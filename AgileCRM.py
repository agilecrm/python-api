import requests
import json
from urlparse import urljoin


APIKEY = "***********"   # Your API KEY
EMAIL = "sample@agilecrm.com"  # Your API EMAIL
DOMAIN = "sample"  # Your DOMAIN

BASE_URL = "https://" + DOMAIN + ".agilecrm.com/dev/api/"

# Function definition is here
def agileCRM(nextURL,method,data,contenttype):

   url = BASE_URL + nextURL

   headers = {
        'Accept': 'application/json',
        'content-type': contenttype,
    }

   if ( method  == "GET" ) :
       
       response = requests.get(
        url,
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text
    
   if ( method  == "POST" ) :
       
       response = requests.post(
        url,
        data=json.dumps(data),
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text
    
   if ( method  == "PUT" ) :
       response = requests.put(
        url,
        data=json.dumps(data),
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text

   if ( method  == "DELETE" ) :
       response = requests.delete(
        url,
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response

   if ( method  == "POSTFORM" ) :
       
       response = requests.post(
        url,
        data=data,
        headers=headers,
        auth=(EMAIL, APIKEY)
        )
       return response.text

   
   return "Wrong method provided"

# ================================================= CREATE CONTACT===============================================
contact_data = {
    "star_value": "4",
    "lead_score": "92",
    "tags": [
        "Lead",
        "Likely Buyer"
    ],
    "properties": [
        {
            "type": "SYSTEM",
            "name": "first_name",
            "value": "Los "
        },
        {
            "type": "SYSTEM",
            "name": "last_name",
            "value": "Bruikheilmer"
        },
        {
            "type": "SYSTEM",
            "name": "company",
            "value": "steady.inc"
        },
        {
            "type": "SYSTEM",
            "name": "title",
            "value": "VP Sales"
        },
        {
            "type": "SYSTEM",
            "name": "email",
            "subtype": "work",
            "value": "akrambakram@yabba.com"
        },
        {
            "type": "SYSTEM",
            "name": "address",
            "value": "{\"address\":\"225 George Street\",\"city\":\"NSW\",\"state\":\"Sydney\",\"zip\":\"2000\",\"country\":\"Australia\"}"
        },
        {
            "type": "CUSTOM",
            "name": "My Custom Field",
            "value": "Custom value"
        }
    ]
}

# print agileCRM("contacts","POST",contact_data,"application/json")

# ================================================= UPDATE CONTACT===============================================

update_contact_data = {
    "id": "5707397775491072",
    "properties": [
        {
            "type": "SYSTEM",
            "name": "last_name",
            "value": "Chan"
        },
        {
            "type": "CUSTOM",
            "name": "My Custom Field",
            "value": "Custom value chane"
        }
    ]
}

#print agileCRM("contacts/edit-properties","PUT",update_contact_data,"application/json")

# ================================================= GET CONTACT BY ID===============================================

#print agileCRM("contacts/5707397775491072","GET",None,"application/json")

# ================================================= GET CONTACT BY Email===============================================

#print agileCRM("contacts/search/email/support+id20297@agilecrm.zendesk.com","GET",None,"application/json")

# ================================================= SEARCH CONTACT BY OF EMAIL===============================================

email_data = "email_ids=[%s]" % "poonam.baranwal@invenio-solutions.com"

#print agileCRM("contacts/search/email","POSTFORM",email_data,"application/x-www-form-urlencoded")

# ================================================= CREATE COMPANY===============================================

company_data = {
    "type": "COMPANY",
    "star_value": 4,
    "lead_score": 120,
    "tags": [
        "Permanent",
        "USA",
        "Hongkong",
        "Japan"
    ],
    "properties": [
        {
            "name": "Company Type",
            "type": "CUSTOM",
            "value": "MNC Inc"
        },
        {
            "type": "SYSTEM",
            "name": "name",
            "value": "Spicejet"
        },
        {
            "type": "SYSTEM",
            "name": "url",
            "value": "http://www.spicejet.com/"
        },
        {
            "name": "email",
            "value": "care@spicejet.com  ",
            "subtype": ""
        },
        {
            "name": "phone",
            "value": "45500000",
            "subtype": ""
        },
        {
            "name": "website",
            "value": "http://www.linkedin.com/company/agile-crm",
            "subtype": "LINKEDIN"
        },
        {
            "name": "address",
            "value": "{\"address\":\"MS 35, 440 N Wolfe Road\",\"city\":\"Sunnyvale\",\"state\":\"CA\",\"zip\":\"94085\",\"country\":\"US\"}",
            "subtype": "office"
        }
    ]
}

#print agileCRM("contacts","POST",company_data,"application/json")

# ================================================= UPDATE COMPANY===============================================

update_company_data = {
    "id": 5661396394049536,
    "properties": [
        {
            "type": "SYSTEM",
            "name": "name",
            "value": "SPICE JET"
        },
        {
            "type": "SYSTEM",
            "name": "url",
            "value": "http://www.spicejet.com/"
        },
        {
            "name": "phone",
            "value": "45500000",
            "subtype": ""
        }
    ]
}

#print agileCRM("contacts/edit-properties","PUT",update_company_data,"application/json")

# ================================================= CREATE DEAL===============================================

deal_data = {
    "name": "Deal-Tomato",
    "expected_value": "500",
    "probability": "75",
    "close_date": 1455042600,
    "milestone": "Proposal",
    "contact_ids": [
        "5661679325020160"
    ],
    "custom_data": [
        {
            "name": "Group Size",
            "value": "10"
        }
    ]
}

#print agileCRM("opportunity","POST",deal_data,"application/json")

# ================================================= Update DEAL===============================================

update_data = {
    "id": "5647457211908096",
    "expected_value": "1000",
    "probability": "20",
    "milestone": "Proposal",
    "contact_ids": [
        "5661679325020160",
        "5684821548335104"
    ],
    "custom_data": [
        {
            "name": "dealTester",
            "value": "hello hello2"
        }
    ]
}

#print agileCRM("opportunity/partial-update","PUT",update_data,"application/json")

# ================================================= CREATE Note to contact===============================================

note_data = {
    "subject": " Note subject",
    "description": "Note description",
    "contact_ids": [
        "5707143030243328",
        "5721389839417344"
    ]
}

#print agileCRM("notes","POST",note_data,"application/json")

# ================================================= CREATE Note to deal===============================================

note_deal_data = {
    "subject": "Deal From Albany",
    "description": "This deal came directly from customer. No advertisement and hence very important for us.",
    "deal_ids": [
        "5178487182721024"
    ]
}

#print agileCRM("opportunity/deals/notes","POST",note_deal_data,"application/json")

