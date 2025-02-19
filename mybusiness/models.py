from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Referencing User Model:
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#referencing-the-user-model
# https://learndjango.com/tutorials/django-best-practices-referencing-user-model
# Custom User Model:
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
# https://learndjango.com/tutorials/django-custom-user-model
# Reset Migration:
# https://raturi.in/blog/how-reset-django-migrations/
# Many-to-Many Relationships:
# https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/

# General Status
class Status(models.Model):
    status_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# Cusstom User Based on: 
# https://learndjango.com/tutorials/django-custom-user-model
class MyUser(AbstractUser):
    #pass
    # add additional fields in here

    def __str__(self):
        return self.username

# checked
class Gender(models.Model):
    gender_name = models.CharField(max_length=64)
    gender_code = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# checked
class Client(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64)
    birthdate = models.DateField()
    sin = models.CharField(max_length=64)
    #gender = models.ForeignKey(Gender, on_delete=models.PROTECT, related_name="clients")
    gender = models.CharField(max_length=64, null = True)
    # Owner Datetime
    created_by = models.ForeignKey(MyUser, on_delete=models.PROTECT, related_name="created_clients")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# checked
class Country(models.Model):
    country_name = models.CharField(max_length=64)
    country_code = models.CharField(max_length=64)

# checked
class ProvinceState(models.Model):
    province_state_name = models.CharField(max_length=64)
    province_state_code = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="provinces_states")
    
# checked
class AddressType(models.Model):
    address_type_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# checked
class Address(models.Model):
    #client = models.ForeignKey(Client, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=64, null=True, blank=True)
    street_address = models.CharField(max_length=1024)
    city = models.CharField(max_length=64)
    province_state = models.ForeignKey(ProvinceState, on_delete=models.PROTECT, related_name="addresses")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="addressess")
    postal_code = models.CharField(max_length=64)
    address_type = models.ForeignKey(AddressType, on_delete=models.PROTECT,null=True,blank=True, related_name="addresses")
    description = models.CharField(max_length=1024, null=True, blank=True)

class ClientAddress(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    # Link to ClientSerializer's client_addresses
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='client_addresses')
    description = models.CharField(max_length=1024, null=True)

# checked
class PhoneType(models.Model):
    phone_type_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# checked
class Phone(models.Model):
    #client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="phones")
    clients = models.ManyToManyField(Client, related_name='phone_list')
    area_code = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    phone_type = models.ForeignKey(PhoneType, on_delete=models.PROTECT,null=True, related_name="phones")
    is_primary = models.BooleanField()
    is_active = models.BooleanField()
    is_archived = models.BooleanField()
    notes = models.CharField(max_length=1024, null=True, default = None)

# checked
class EmailType(models.Model):
    email_type_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# checked
class Email(models.Model):
    #client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="emails")
    clients = models.ManyToManyField(Client)
    email = models.CharField(max_length=1024)
    email_type = models.ForeignKey(EmailType, on_delete=models.PROTECT, related_name="emails")
    is_primary = models.BooleanField()
    is_active = models.BooleanField()
    notes = models.CharField(max_length=1024, null=True)

# checked
class ProductType(models.Model):
    product_type_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# checked
class Product(models.Model):
    product_name = models.CharField(max_length=64)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name="products")
    description = models.CharField(max_length=1024, null=True)

# Checked
class BusinessStatus(models.Model):
    status_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# Checked
class BusinessType(models.Model):
    business_type_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)    

# Checked
class MyBusiness(models.Model):
    business_type = models.ForeignKey(BusinessType, on_delete=models.PROTECT, related_name="mybusinesses", null=True)
    product = models.ForeignKey(Product, on_delete = models.PROTECT, related_name="mybusinesses", null=True)
    # This is the applicant client, can be different from the insured client which is in InsuranceApplication model
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="businesses")
    status = models.ForeignKey(BusinessStatus, on_delete=models.PROTECT, related_name="mybusinesses")
    projected_FYC = models.FloatField(null=True)
    settled_FYC = models.FloatField(null=True)
    application_date = models.DateField(null=True)
    settled_date = models.DateField(null=True)
    application_location = models.CharField(max_length=64, null=True)
    applicant_client_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="mybusinesses", null=True)
    applicant_client_phone = models.ForeignKey(Phone, on_delete=models.PROTECT, related_name="mybusinesses", null=True)
    # Owner Datetime
    # The related name in created_by, my_businesses, corresponds to the my_businesses field in UserSerializer
    # This is so that the User json from API will display a list of related mybusiness created by the user.
    created_by = models.ForeignKey(MyUser, on_delete=models.PROTECT, related_name="created_businesses", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    highlighted = models.BooleanField(default=False)

# Checked
class BusinessUserRole(models.Model):
    user_role_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)
    default_split = models.IntegerField(null=True) # 0 to 10000, with two implied decimals

# On the NBF, each collaborator can have a status such as:
# QT - Qualified Trainer
# Independent - Independent Advisor
# Supervisor
# ... etc
class CollaboratorStatus(models.Model):
    status_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True) 

class CollaboratorPosition(models.Model):
    position_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)


# Checked
# M-2-M Association
class Business_User(models.Model):
    business = models.ForeignKey(MyBusiness, on_delete=models.CASCADE, related_name="related_users")
    # Reverse relationship from MyUser with the attribute my_businesses
    # Eg:
    # >>> bob = MyUser.objects.filter(username='bob')[0]
    # >>> bob.my_businesses
    # <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7f82562bf190>
    # >>> bob.my_businesses.all()[0].split
    # To Do: Refactor the name from my_businesses to related_businesses
    user = models.ForeignKey(MyUser, on_delete = models.PROTECT, related_name="my_businesses")
    split = models.IntegerField(null=True) # 0 to 10000, with two implied decimals
    user_role = models.ForeignKey(BusinessUserRole, on_delete=models.PROTECT, related_name = "businessusers", null=True)
    notes = models.CharField(max_length=1024, null=True)
    # Owner Datetime
    created_by = models.ForeignKey(MyUser, on_delete=models.PROTECT, related_name="created_businessusers", null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # Additional fields
    collaborator_status = models.ForeignKey(CollaboratorStatus, on_delete=models.PROTECT, related_name="businessusers", null=True)
    collaborator_position = models.ForeignKey(CollaboratorPosition, on_delete=models.PROTECT, related_name="businessusers", null=True)
    cfc_code = models.CharField(max_length=64, null=True)
# Checked
class ComplianceEntity(models.Model):
    compliance_entity_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# Checked
# M-2-M Association
# DO NOT USE THIS ANYMORE. THIS IS A BIT MESSED UP!
#class Business_ComplianceEntity(models.Model):
#    compliance_entity = models.ForeignKey(ComplianceEntity, on_delete=models.PROTECT, name="businesses")
#    businesss = models.ForeignKey(MyBusiness, on_delete=models.CASCADE, name="complianceentities")
#    notes = models.CharField(max_length=1024, null=True)

class BusinessComplianceEntity(models.Model):
    business = models.ForeignKey(MyBusiness, on_delete=models.CASCADE, related_name="businesscomplianceentities")
    compliance_entity = models.ForeignKey(ComplianceEntity, on_delete=models.PROTECT, related_name="businesscomplianceentities")
    notes = models.CharField(max_length=1024,blank=True, null=True)

# Checked
class Document(models.Model):
    document_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# Checked
# M-2-M Association
class Business_Document(models.Model):
    business = models.ForeignKey(MyBusiness, on_delete=models.CASCADE, related_name="documents")
    document = models.ForeignKey(Document, on_delete=models.PROTECT, related_name="mybusinesses")
    is_submitted = models.BooleanField(default=False)
    url = models.CharField(max_length=1024, null=True, blank=True) # Location of the document
    notes = models.CharField(max_length=1024, null=True, blank=True)
# Checked
class InsuranceProvider(models.Model):
    insurance_provider_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# Checked
class InsurancePlanType(models.Model):
    insurnace_plan_type_name = models.CharField(max_length=64)
    insurance_plan_type_code = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=1024, null=True)

# Checked
class InsurancePlan(models.Model):
    insurance_plan_name = models.CharField(max_length=64)
    insurance_plan_code = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=1024, null=True)

# Checked
class InsuranceApplication(models.Model):
    insured_client = models.ForeignKey(Client, on_delete=models.PROTECT, default=None, null=True, related_name="insurance_applications")
    business = models.ForeignKey(MyBusiness, on_delete=models.CASCADE, related_name="insurance_application") #1-2-1 relationship
    product = models.ForeignKey(Product, on_delete=models.PROTECT,null=True, related_name = "insurance_applications")
    provider = models.ForeignKey(InsuranceProvider, on_delete=models.PROTECT, null=True, related_name="insurance_applications")
    plan_type = models.ForeignKey(InsurancePlanType, on_delete=models.PROTECT, null=True, related_name="insurance_applications")
    plan = models.ForeignKey(InsurancePlan, on_delete=models.PROTECT,null=True, related_name="insurance_applications")
    face_amount = models.FloatField(null=True)
    planned_premium = models.FloatField(null=True)
    # application address and phone use charfield to allow overwriting with client's address and phone
    # applicant_address = models.CharField(max_length=1024, null=True) 
    # applicant_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="insurance_applications", null=True)
    #applicant_phone = models.CharField(max_length=64, null=True)
    #applicant_phone = models.ForeignKey(Phone, on_delete=models.PROTECT, related_name="insurance_applications", null=True)
    insured_client_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="insurance_applications", null=True)
    insured_client_phone = models.ForeignKey(Phone, on_delete=models.PROTECT, related_name="insurance_applications", null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# Checked
class Medical(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medical_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True)

# Checked
#class InsuranceApplication_Medical(models.Model):
#    insurance_application = models.ForeignKey(InsuranceApplication, on_delete=models.CASCADE, related_name="insurance_applications")
#    medical = models.ForeignKey(Medical, on_delete=models.PROTECT, related_name="insurance_applications")
#    notes = models.CharField(max_length=1024, null=True)
#    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="insurance_applications", null=True)

class Business_Medical(models.Model):
    business = models.ForeignKey(MyBusiness, on_delete=models.CASCADE, related_name="business_medicals")
    medical = models.ForeignKey(Medical, on_delete=models.PROTECT, related_name="business_medicals")
    notes = models.CharField(max_length=1024, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="business_medicals", null=True)

# Checked
class ActivityLog(models.Model):
    event_datetime = models.DateTimeField()
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name="activities")
    model_name = models.CharField(max_length=64, null=True)
    field_name = models.CharField(max_length=64, null=True)
    value = models.CharField(max_length=1024, null=True)
    notes = models.CharField(max_length=1024, null=True)

class BusinessInsurance(models.Model):
    business = models.ForeignKey(MyBusiness, on_delete=models.PROTECT, related_name="business_insurance")
    insurance_plan = models.ForeignKey(InsurancePlan, on_delete=models.PROTECT, related_name="business_insurance")
    insurance_application = models.ForeignKey(InsuranceApplication, on_delete=models.PROTECT, related_name="business_insurance")
    policy_number = models.CharField(max_length=64)
    notes = models.CharField(max_length=1024, null=True)
    created_by = models.ForeignKey(MyUser, on_delete=models.PROTECT, related_name="created_businessinsurance")
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()


class BusinessSupervisor(models.Model):
    business = models.ForeignKey(MyBusiness, on_delete=models.PROTECT, related_name="business_supervisor")
    supervisor = models.ForeignKey(MyUser, on_delete=models.PROTECT, related_name="business_supervisor")
    notes = models.CharField(blank=True, max_length=1024, null=True)

class Notification(models.Model):
    from_user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='sent_notifications', null=True)
    to_user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='received_notifications', null=True)
    related_business = models.ForeignKey(MyBusiness, on_delete=models.DO_NOTHING, related_name='notifications')
    read = models.BooleanField(default=False)
    message_code = models.CharField(max_length=64) # Code that suggest the type of message
    message_text = models.CharField(max_length=1024)
    created_date = models.DateTimeField(auto_now_add=True)
    broadcast_group = models.CharField(max_length=64, null=True) # Group of users that will receive the messagea
    # How do I create a link that opens up the business?

class UserNotification(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='user_notifications')
    notification = models.ForeignKey(Notification, on_delete=models.DO_NOTHING, related_name='user_notifications')
    read = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

class BusinessDeclined(models.Model):
    business = models.ForeignKey(MyBusiness, on_delete=models.PROTECT, related_name="business_declined")
    notes = models.CharField(max_length=1024, null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    


