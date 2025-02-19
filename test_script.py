from mybusiness.models import *
bt = BusinessType(business_type_name='Insurance',description='Insurancess Business')
bt.save()

pt = ProductType(product_type_name='Life Insurance', description='A type of insurance')
pt.save()

p = Product(product_name='Life 1', product_type = pt, description = 'Life Insurance and dental')
p.save()

bs = BusinessStatus(status_name='Review', description='Under Review')
bs.save()

g = Gender(gender_name='Male', gender_code='M', description='Has Penis')
g.save()

import datetime
c = Client(gender = g, first_name='Joe',middle_name='Yi',last_name='Fang',birthdate=datetime.datetime.now(), created_by = MyUser.objects.all()[0], created_date=datetime.datetime.now(), modified_date = datetime.datetime.now())
c.save()

bur = BusinessUserRole(user_role_name = 'owner', description='a user who is responsible for the business', default_split=100)
bur.save()

plan = InsurancePlan(insurance_plan_name ='Par Whole Life', insurance_plan_code = 'par001', description = 'this is a test plan')
plan.save()

insuranceprovider = InsuranceProvider(insurance_provider_name='Canada Life',description='Test Provider')
insuranceprovider.save()


# Adding a user to a business
from mybusiness.models import *
businesses = MyBusiness.objects.all()
test_business = businesses[4]
users = MyUser.objects.all()
chris = users[7]
creator = users[0]
import datetime
now = datetime.datetime.now()
roles = BusinessUserRole.objects.all()
role = roles[0]
bu = Business_User(business=test_business, user = chris, split=50, user_role = role, notes = 'test', created_by = creator, created_date = now, modified_date = now)
bu.save()


