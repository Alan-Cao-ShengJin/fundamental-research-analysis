"""Displayed thresholds must imply the advertised rating; approximate watch levels are allowed."""
import copy
from pathlib import Path
import sys
import unittest

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'report-layout/scripts'),str(Path(__file__).resolve().parents[1]/'company-model/scripts')]
import decision_triggers as dt


class DecisionTriggerTests(unittest.TestCase):
    def setUp(self):
        values={'A1':100,'A2':.50,'A3':.05,'A4':'=A2/A3','A5':'=IF(A4/A1-1>0.1,"Buy",IF(A4/A1-1<-0.1,"Sell","Hold"))',
                'A6':'=A1*1.1*A3','A7':.04525,'A8':'=A2/(A1*.9)'}
        # Use ordinary profit/price units: DPS 5.00 on a 5% required yield and a 100 quote.
        values['A2']=5
        self.spec={'sheets':{'V':{'cells':{k:{'value':v} for k,v in values.items()}}}}
        self.record={'bindings':{'referencePrice':'V!A1','target':'V!A4','rating':'V!A5'}}
        self.decision={'boundText':[{'pointer':'/triggers/text','template':'Buy at {threshold}.',
            'inputs':{'threshold':{'model':'V!A6','style':'number','decimals':0}}}],
            'triggerCoverage':{'status':'checked','testIds':['buy']},
            'triggerTests':[{'id':'buy','mode':'automatic','boundary':{'pointer':'/triggers/text','token':'threshold'},
                'inputRef':'V!A2','relation':'>=','expectedRating':'Buy','rationale':'Change this economic driver alone.'}]}

    def test_rounded_down_automatic_buy_trigger_is_rejected(self):
        # Exact 5.50 formats as 6 under Python round-to-even: use 5.49 -> 5, below the true Buy boundary.
        self.spec['sheets']['V']['cells']['A6']['value']=5.49
        with self.assertRaisesRegex(ValueError,'gives Hold'): dt.verify(self.decision,self.spec,self.record)

    def test_exact_boundary_is_hold_under_strict_house_call(self):
        self.decision['boundText'][0]['inputs']['threshold']['decimals']=2
        with self.assertRaisesRegex(ValueError,'not Buy'): dt.verify(self.decision,self.spec,self.record)

    def test_decimal_house_boundaries_do_not_flip_from_binary_return_noise(self):
        import release_check as rc
        self.assertEqual(rc.rating_for(rc.price_return(110,100)),'Hold')
        self.assertEqual(rc.rating_for(rc.price_return(90,100)),'Hold')
        self.assertEqual(rc.rating_for(rc.price_return(110.0001,100)),'Buy')
        self.assertEqual(rc.rating_for(rc.price_return(89.9999,100)),'Sell')

    def test_strict_condition_just_above_boundary_is_valid(self):
        self.decision['boundText'][0]['inputs']['threshold']['decimals']=2
        self.decision['triggerTests'][0]['relation']='>'
        self.assertEqual(dt.verify(self.decision,self.spec,self.record)[0]['probes'][0]['rating'],'Buy')

    def test_conservatively_precise_sufficient_trigger_is_allowed(self):
        self.spec['sheets']['V']['cells']['A6']['value']=5.51
        self.decision['boundText'][0]['inputs']['threshold']['decimals']=2
        self.assertTrue(dt.verify(self.decision,self.spec,self.record))

    def test_percent_trigger_uses_fractional_model_coordinates(self):
        self.decision['boundText'][0]['inputs']['threshold']={'model':'V!A7','style':'percent','decimals':1}
        t=self.decision['triggerTests'][0]; t.update(inputRef='V!A3',relation='<',expectedRating='Buy')
        self.assertEqual(dt.verify(self.decision,self.spec,self.record)[0]['displayed'],'4.5%')
        self.spec['sheets']['V']['cells']['A7']['value']=.046
        with self.assertRaisesRegex(ValueError,'not Buy'): dt.verify(self.decision,self.spec,self.record)

    def test_watch_level_does_not_promise_automatic_rating(self):
        self.decision['triggerTests'][0]={'id':'buy','mode':'watch','boundary':{'pointer':'/triggers/text','token':'threshold'},
            'rationale':'Rounded level invites reassessment; no automatic call is stated.'}
        self.assertFalse(dt.verify(self.decision,self.spec,self.record)[0]['automaticRatingVerified'])
        self.decision['triggerTests'][0]['expectedRating']='Buy'
        with self.assertRaisesRegex(ValueError,'watch level'): dt.verify(self.decision,self.spec,self.record)

    def test_no_trigger_claims_validly_not_applicable_but_missing_or_hidden_tests_fail(self):
        empty={'triggerCoverage':{'status':'not-applicable','reason':'No quantitative decision triggers.','testIds':[]},'triggerTests':[]}
        self.assertEqual(dt.verify(empty,self.spec,self.record),[])
        with self.assertRaises(ValueError): dt.verify({},self.spec,self.record)
        self.decision['triggerCoverage']=empty['triggerCoverage']
        with self.assertRaises(ValueError): dt.verify(self.decision,self.spec,self.record)

    def test_tests_cannot_override_rating_or_hide_coverage(self):
        self.decision['triggerTests'][0]['inputRef']='V!A5'
        with self.assertRaisesRegex(ValueError,'rating output'): dt.verify(self.decision,self.spec,self.record)
        self.decision['triggerTests'][0]['inputRef']='V!A2'
        self.decision['triggerCoverage']['testIds']=[]
        with self.assertRaisesRegex(ValueError,'coverage'): dt.verify(self.decision,self.spec,self.record)


if __name__=='__main__': unittest.main()
