from . import constants as const 
from . import models


def get_payload(purchase: models.PurchaseV3) -> dict:
    return_url = const.return_url + purchase.tracker.key
    return {
        "isSandbox" : False,
        "storeID" : const.store_id,
        "successUrl" : return_url,
        "failUrl" : return_url,
        "cancelUrl" : return_url,
        "transactionID" : purchase.transaction_id,
        "transactionAmount" : str(float(purchase.payable_amount)),
        "signature" : const.signature_key,
        "customerState" : str(purchase.tracker.id),
        "customerName" : purchase.user.get_full_name(),
        "customerEmail" : purchase.user.email,
        "customerMobile" : purchase.user.phone.number if hasattr(purchase.user, 'phone') else '018768815107'
    }