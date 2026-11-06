import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';

const catalog = JSON.parse(readFileSync(new URL('../catalog.json', import.meta.url), 'utf8'));

function dependencies(stage, visited = new Set()) {
  for (const name of catalog.stages[stage].requiredBefore) {
    if (!visited.has(name)) { visited.add(name); dependencies(name, visited); }
  }
  return visited;
}

describe('company research risk dependencies', () => {
  it('requires early governance and financial screening before forecasts in every full company route', () => {
    for (const flow of Object.values(catalog.flows).filter(flow => flow.includes('company-forecast'))) {
      for (const risk of ['corporate-governance', 'financial-red-flags']) {
        expect(flow).toContain(risk);
        expect(flow.indexOf(risk)).toBeLessThan(flow.indexOf('revenue-projection'));
        expect(dependencies('revenue-projection').has(risk)).toBe(true);
        expect(dependencies('conclusion').has(risk)).toBe(true);
      }
    }
  });

  it('runs industry analysis before revenue projection in every full company route and refreshes it in reviews', () => {
    for (const flow of Object.values(catalog.flows).filter(flow => flow.includes('company-forecast'))) {
      expect(flow.indexOf('industry-analysis')).toBeGreaterThan(-1);
      expect(flow.indexOf('industry-analysis')).toBeLessThan(flow.indexOf('revenue-projection'));
    }
    expect(dependencies('revenue-projection').has('industry-analysis')).toBe(true);
    for (const name of ['company-regular-review', 'company-update']) expect(catalog.flows[name]).toContain('revision-industry');
    expect(dependencies('revision-impact').has('revision-industry')).toBe(true);
  });

  it('keeps one financial-quality skill across three passes with the audit upstream of valuation', () => {
    for (const stage of ['financial-red-flags', 'model-audit', 'thesis-validation']) {
      expect(catalog.stages[stage].skill).toBe('financial-quality');
      expect(catalog.stages[stage].output).toBe('financial-quality');
    }
    expect(dependencies('model-audit').has('financial-red-flags')).toBe(true);
    expect(dependencies('valuation').has('model-audit')).toBe(true);
    expect(dependencies('thesis-validation').has('valuation')).toBe(true);
  });

  it('permits a filing-based red-flag review without full forecasting or a stock call', () => {
    const flow = catalog.flows['financial-red-flag-review'];
    expect(flow).toContain('financial-red-flags');
    expect(dependencies('financial-red-flags').has('evidence')).toBe(true);
    for (const stage of ['company-model-setup', 'company-forecast', 'valuation', 'conclusion']) {
      expect(flow).not.toContain(stage);
      expect(dependencies('financial-red-flags').has(stage)).toBe(false);
    }
  });
});

describe('initiation and revision workflow boundaries', () => {
  it('routes first coverage through a full baseline and existing coverage through baseline review', () => {
    const initiation = catalog.companyWorkflows.initiation;
    const revision = catalog.companyWorkflows.revision;
    expect(initiation.entrySkill).toBe('stock-initiation');
    expect(revision.entrySkill).toBe('model-revision');
    const fresh = catalog.flows[initiation.flow];
    const update = catalog.flows[revision.flow];
    expect(fresh).toContain('stock-initiation');
    expect(fresh).toContain('company-actuals');
    expect(fresh.indexOf('stock-initiation')).toBeLessThan(fresh.indexOf('company-model-setup'));
    expect(update).toContain('revision-baseline');
    expect(update.indexOf('revision-baseline')).toBeLessThan(update.indexOf('revision-evidence'));
    expect(update).not.toContain('stock-initiation');
    expect(update).not.toContain('company-model-setup');
    expect(update).not.toContain('company-actuals');
    expect(dependencies('model-revision').has('company-model-setup')).toBe(false);
  });

  it('retains a risk review, calculation audit and challenge before a revised decision', () => {
    const deps = dependencies('revision-conclusion');
    for (const required of ['revision-baseline', 'revision-evidence', 'revision-impact', 'revision-forecast-evaluation', 'revision-risk-review', 'model-revision', 'revision-audit', 'revision-valuation', 'revision-challenge']) {
      expect(deps.has(required)).toBe(true);
    }
    expect(catalog.stages['model-revision'].skill).toBe(catalog.stages['company-forecast'].skill);
    expect(catalog.stages['revision-audit'].skill).toBe(catalog.stages['model-audit'].skill);
    expect(catalog.stages['revision-conclusion'].skill).toBe(catalog.stages.conclusion.skill);
    expect(dependencies('revision-brief').has('revision-conclusion')).toBe(true);
  });

  it('requires mode selection and lets a regular review reuse forecasts without forced rebuilding', () => {
    const revision = catalog.companyWorkflows.revision;
    expect(revision.requiresModeSelection).toBe(true);
    const regular = revision.modes.regular;
    expect(regular.forecastPolicy).toBe('retain-unless-supported-change');
    const flow = catalog.flows[regular.flow];
    for (const stage of ['revision-baseline', 'revision-evidence', 'revision-impact', 'regular-valuation', 'regular-conclusion']) expect(flow).toContain(stage);
    for (const stage of ['stock-initiation', 'model-revision', 'revision-forecast-evaluation']) expect(flow).not.toContain(stage);
    expect(dependencies('regular-valuation').has('revision-baseline')).toBe(true);
    expect(dependencies('regular-valuation').has('model-revision')).toBe(false);
    expect(dependencies('regular-conclusion').has('regular-challenge')).toBe(true);
    expect(regular.forecastChangeRequires).toEqual(expect.arrayContaining(['concrete-evidence', 'affected-risk-review', 'model-recalculation', 'model-audit', 'downstream-refresh']));
    // A supported forecast change inserts the model stages the flow list omits; they are catalog stages, not prose.
    expect(regular.forecastChangeStages).toEqual(['revision-risk-review', 'model-revision', 'revision-audit']);
    for (const stage of regular.forecastChangeStages) expect(catalog.stages[stage]).toBeDefined();
    expect(catalog.stages['model-revision'].skill).toBe('company-model');
    expect(catalog.stages['revision-audit'].skill).toBe('financial-quality');
    expect(revision.modes[regular.escalateTo].flow).toBe('company-update');
  });

  it('evaluates the frozen forecast before model replacement in the major update route', () => {
    const major = catalog.companyWorkflows.revision.modes.major;
    expect(major.forecastPolicy).toBe('evaluate-then-recalibrate');
    const flow = catalog.flows[major.flow];
    expect(flow.indexOf(major.learningStage)).toBeGreaterThan(flow.indexOf('revision-evidence'));
    expect(flow.indexOf(major.learningStage)).toBeLessThan(flow.indexOf('model-revision'));
    expect(dependencies('model-revision').has(major.learningStage)).toBe(true);
    expect(catalog.stages[major.learningStage].skill).toBe('model-revision');
  });
});

describe('publication within research modes', () => {
  it('publishes a stock brief only after the conclusion, while evidence summaries need no stock call', () => {
    expect(dependencies('investment-brief').has('conclusion')).toBe(true);
    expect(dependencies('brief').has('conclusion')).toBe(false);
    for (const name of ['new-company-research', 'company-to-portfolio'].filter(name => catalog.flows[name])) expect(catalog.flows[name]).toContain('investment-brief');
    for (const name of ['industry-review', 'corporate-governance-review', 'financial-red-flag-review']) expect(catalog.flows[name]).toContain('brief');
  });
  it('renders and release-checks deliverables after the brief in every company mode', () => {
    for (const [flowName, brief, render] of [
      ['new-company-research', 'investment-brief', 'report-render'],
      ['company-regular-review', 'regular-brief', 'regular-report-render'],
      ['company-update', 'revision-brief', 'revision-report-render']
    ]) {
      expect(catalog.flows[flowName].indexOf(render)).toBeGreaterThan(catalog.flows[flowName].indexOf(brief));
      expect(catalog.stages[render].skill).toBe('report-layout');
      expect(dependencies(render).has(brief)).toBe(true);
    }
    expect(catalog.stages['report-exhibits'].skill).toBe('chart-visualization');
  });
});

describe('conviction within research modes', () => {
  it('retains follow-up and learning after the decision in all three core research modes', () => {
    for (const [flowName, followup, conclusion] of [
      ['new-company-research', 'company-follow-up', 'conclusion'],
      ['company-regular-review', 'regular-follow-up', 'regular-conclusion'],
      ['company-update', 'revision-follow-up', 'revision-conclusion']
    ]) {
      expect(catalog.flows[flowName].at(-1)).toBe(followup);
      expect(catalog.stages[followup].skill).toBe('monitor-review');
      expect(dependencies(followup).has(conclusion)).toBe(true);
    }
  });
  it('reviews the decisive belief before every full company conclusion using the same specialist', () => {
    const cases = [
      ['new-company-research', 'conviction', 'conclusion'],
      ['company-update', 'revision-conviction', 'revision-conclusion'],
      ['company-regular-review', 'regular-conviction', 'regular-conclusion']
    ];
    if (catalog.flows['company-to-portfolio']) cases.push(['company-to-portfolio', 'conviction', 'conclusion']);
    for (const [flowName, convictionStage, conclusionStage] of cases) {
      const flow = catalog.flows[flowName];
      expect(flow).toContain(convictionStage);
      expect(flow.indexOf(convictionStage)).toBeLessThan(flow.indexOf(conclusionStage));
      expect(dependencies(conclusionStage).has(convictionStage)).toBe(true);
      expect(catalog.stages[convictionStage].skill).toBe('investment-conviction');
      // Reuse the existing conclusion envelope for referenced conviction support.
      expect(catalog.stages[convictionStage].output).toBe('investment-conclusion');
    }
  });

  it('tests conviction against the financial/governance challenge without forcing routine forecast rebuilding', () => {
    for (const required of ['corporate-governance', 'model-audit', 'thesis-validation', 'challenge']) {
      expect(dependencies('conviction').has(required)).toBe(true);
    }
    for (const required of ['revision-baseline', 'revision-evidence', 'regular-challenge']) {
      expect(dependencies('regular-conviction').has(required)).toBe(true);
    }
    expect(dependencies('regular-conviction').has('model-revision')).toBe(false);
    for (const required of ['revision-forecast-evaluation', 'revision-risk-review', 'revision-audit', 'revision-challenge']) {
      expect(dependencies('revision-conviction').has(required)).toBe(true);
    }
  });
});
