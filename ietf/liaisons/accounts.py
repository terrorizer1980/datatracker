from ietf.idtracker.models import Role


def get_person_for_user(user):
    return user.get_profile().person()


def is_areadirector(person):
    return bool(person.areadirector_set.all())


def is_wgchair(person):
    return bool(person.wgchair_set.all())


def is_wgsecretary(person):
    return bool(person.wgsecretary_set.all())


def has_role(person, role):
    return bool(person.role_set.filter(pk=role))


def is_ietfchair(person):
    return has_role(person, Role.IETF_CHAIR)


def is_iabchair(person):
    return has_role(person, Role.IAB_CHAIR)


def is_iab_executive_director(person):
    return has_role(person, Role.IAB_EXCUTIVE_DIRECTOR)


def can_add_liaison(user):
    person = get_person_for_user(user)
    if not person:
        return False

    if (is_areadirector(person) or is_wgchair(person) or
        is_wgsecretary(person) or is_ietfchair(person) or
        is_iabchair(person) or is_iab_executive_director(person)):
        return True
    return False
