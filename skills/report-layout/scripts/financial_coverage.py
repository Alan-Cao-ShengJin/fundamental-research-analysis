"""Separate economic applicability from completion of required financial verification."""


def verify(family, declaration, packet):
    actual=[a['id'] for a in packet.get('financialAssertions',[]) if a.get('kind')==family]
    linked=declaration.get('assertionIds',[])
    claims=declaration.get('claimIds',[])
    known={c['id'] for c in packet['handoff']['claims']}
    if (not isinstance(linked,list) or len(set(linked))!=len(linked) or
            not isinstance(claims,list) or len(set(claims))!=len(claims)):
        return False,'Financial coverage needs unique assertionIds and claimIds'
    applies=declaration.get('applicability')
    if applies=='not-applicable':
        ok=(declaration.get('status')=='not-applicable' and bool(str(declaration.get('reason','')).strip())
            and not actual and not linked and not claims)
        return ok,'Economic non-applicability needs a reason and no applicable claims or hidden family assertions'
    if applies!='applicable':
        return False,'Determine economic applicability before assessing implementation'
    ok=(declaration.get('status')=='checked' and bool(actual) and set(linked)==set(actual)
        and bool(claims) and set(claims)<=known)
    return ok,('An applicable financial claim needs checked family assertions and registered claimIds; missing rows, '
               'data or display bindings mean verification is incomplete, not not-applicable')
