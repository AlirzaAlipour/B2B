from rest_framework_api_key.permissions import BaseHasAPIKey
from merchants.models import MerchantAPIKey


class HasMerchantAPIKey(BaseHasAPIKey):
    model = MerchantAPIKey 
