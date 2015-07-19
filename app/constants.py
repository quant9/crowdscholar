# user role
ADMIN = 0
STUDENT = 1
DONOR = 2
OTHERUSER = 3
USERTYPE = {
    ADMIN: 'admin',
    STUDENT: 'student',
    DONOR: 'donor',
    OTHERUSER: 'other',
}

# user status
INACTIVE = 0
NEW = 1
ACTIVE = 2
STATUS = {
    INACTIVE: 'inactive',
    NEW: 'new',
    ACTIVE: 'active',
}

# scholarship status
FUNDING = 0
READY = 1
PAID_OUT = 2
EXPIRED = 3
WITHDRAWN = 4
SCHOLARSHIP_STATUS = {
    FUNDING: 'in funding',
    READY: 'fully funded',
    PAID_OUT: 'paid out',
    EXPIRED: 'expired',
    WITHDRAWN: 'withdrawn',
    }
