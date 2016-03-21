Agile CRM Python API 
=================

[Agile CRM] (https://www.agilecrm.com/) is a new breed CRM software with sales and marketing automation.

Table of contents
---------------

**[Requirements](#requirements)**

**[1 Contact](#1-contact)**
  * [1 To create a contact](#11-to-create-a-contact)
  * [2 To fetch contact data](#12-to-fetch-contact-data)
  * [3 To delete a contact](#13-to-delete-a-contact)
  * [4 To update a contact](#14-to-update-a-contact)
  * [5 Update lead score by ID](#15-update-lead-score-by-id)
  * [6 Update star value by ID](#16-update-star-value-by-id)
  * [7 Update tags value by ID](#17-update-tags-value-by-id)
  * [8 Delete tags value by ID](#18-delete-tags-value-by-id)
  * [9 Search contacts/companies](#19-search-contactscompanies)
  * [10 Adding tags to a contact based on email](#110-adding-tags-to-a-contact-based-on-email)
  * [11 Delete tags to a contact based on email](#111-delete-tags-to-a-contact-based-on-email)
  * [12 Add score to a contact using email ID](#112-add-score-to-a-contact-using-email-id)
  

**[2. Company](#2-company)**
  * [1 To create a company](#21-to-create-a-company)
  * [2 To update a company](#22-to-update-a-company)
  * [3 To get a company by company id](#23-to-get-a-company-by-company-id)
  * [4 To delete a company by company id](#24-to-delete-a-company-by-company-id)
 
**[3. Deal (Opportunity)](#3-deal)**
  * [1 To create a deal](#31-to-create-a-deal)
  * [2 To update a deal](#32-to-update-a-deal)
  * [3 Create deal to a contact using email ID](#33-create-deal-to-a-contact-using-email-id)
  * [4 Get list of deal](#34-get-list-of-deal)
  * [5 Get deal by ID](#35-get-deal-by-id)
  * [6 Delete deal by ID](#36-delete-deal-by-id)

**[4. Note ](#4-note)**
  * [1 Create a note and relate that to contacts](#41-create-a-note-and-relate-that-to-contacts)
  * [2 Add note to a contact using email ID](#42-add-note-to-a-contact-using-email-id)
  * [3 Gets notes related to specific contact](#43-gets-notes-related-to-specific-contact)
  * [4 Delete a specific note from specific contact](#44-delete-a-specific-note-from-specific-contact)
  * [5 Create note to a deal](#45-create-note-to-a-deal)
  * [6 Update note to a deal](#46-update-note-to-a-deal)
  * [7 Gets notes related to specific deal](#47-gets-notes-related-to-specific-deal)

Requirements
------------

1. AgileCRM.py file

2. Request library python

2. Setting domain name and Rest API key

![Finding Domain name, email and api key] (https://raw.githubusercontent.com/agilecrm/python-api/master/AgileCRM.png)

In the above image, api key is present at the "Api & Analytics" tab at `https://mycompany.agilecrm.com/#account-prefs`.

So you have to update your [AgileCRM.py](https://github.com/agilecrm/python-api/blob/master/AgileCRM.py)

```javascript
import requests
import json
from urlparse import urljoin


APIKEY = "************"   # Your agile crm Rest API key
EMAIL = "sample@agilecrmcom"  # Your agile crm  email
DOMAIN = "sample"  # Your domain
#-----------------------------------Rest Code--------------------------------
```

API's details
-------------
## 1. Contact
#### 1.1 To create a contact 

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation)

```javascript
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

print agileCRM("contacts","POST",contact_data,"application/json")

```

#### 1.2 To fetch contact data

###### by ID

```javascript
// Get contact by ID
print agileCRM("contacts/5707397775491072","GET",None,"application/json")
```
###### by email

```javascript
// Get contact by Email
print agileCRM("contacts/search/email/sample@agilecrm.zendesk.com","GET",None,"application/json")
```

###### by email ID alternative

```javascript
// Get contact by Email
email_data = "email_ids=[%s]" % "poonam.baranwal@invenio-solutions.com"

print agileCRM("contacts/search/email","POSTFORM",email_data,"application/x-www-form-urlencoded")
```

#### 1.3 To delete a contact

```javascript
// Delete a contact
print agileCRM("contacts/5716466867372032","DELETE",None,"application/json")
```

#### 1.4 To update a contact 

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation-1)

```javascript
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

print agileCRM("contacts/edit-properties","PUT",update_contact_data,"application/json")
```

#### 1.5 Update lead score by ID

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#15-update-lead-score-by-id)

```javascript
update_lead_score = {
    "id": "5708993221623808",
    "lead_score": 20
}

print agileCRM("contacts/edit/lead-score","PUT",update_lead_score,"application/json")
```

#### 1.6 Update star value by ID

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#16-update-star-value-by-id)

```javascript
update_star_value = {
    "id": "5708993221623808",
    "star_value": 2
}

print agileCRM("contacts/edit/add-star","PUT",update_star_value,"application/json")
```

#### 1.7 Update tags value by ID

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation-4)

```javascript
update_tag_value = {
    "id": "5708993221623808",
    "tags": [
        "test1",
        "test2"
    ]
}

print agileCRM("contacts/edit/tags","PUT",update_tag_value,"application/json")
```

#### 1.8 Delete tags value by ID

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation-5)

```javascript
delete_tag_value = {
    "id": "5708993221623808",
    "tags": [
        "test1",
        "test2"
    ]
}

print agileCRM("contacts/delete/tags","PUT",delete_tag_value,"application/json")
```

#### 1.9 Search contacts/companies

```javascript
string result = agileCRM("search?q=ghanshyam raut&page_size=10&type='PERSON'", "GET", null,"application/json");

print agileCRM("search?q=ghanshyam raut&page_size=10&type='PERSON'","GET",None,"application/json")
```

#### 1.10 Adding tags to a contact based on email

```javascript
Work in progress
```

#### 1.11 Delete tags to a contact based on email

```javascript
Work in progress
```

#### 1.12 Add score to a contact using email ID

```javascript
Work in progress
```

## 2. Company
#### 2.1 To create a company 

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation-7)

```javascript
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

print agileCRM("contacts","POST",company_data,"application/json")
```

#### 2.2 To update a company 

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation-8)

```javascript
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

print agileCRM("contacts/edit-properties","PUT",update_company_data,"application/json")
```

#### 2.3 To get a company by company ID

```javascript
print agileCRM("contacts/5661396394049536","GET",None,"application/json")
```

#### 2.4 To delete a company by company ID

```javascript
print agileCRM("contacts/5661396394049536","DELETE",None,"application/json")
```

## 3. Deal
#### 3.1 To create a deal 

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation-9)

```javascript
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

print agileCRM("opportunity","POST",deal_data,"application/json")
```

#### 3.2 To update a deal 

- [**Acceptable request representation for contact**](https://github.com/agilecrm/rest-api#acceptable-request-representation-10)

```javascript
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

print agileCRM("opportunity/partial-update","PUT",update_data,"application/json")
```

#### 3.3 Create deal to a contact using email ID 

```javascript
Work in progress
```

#### 3.4 Get list of deal

- [**Reference**](https://github.com/agilecrm/rest-api#31-listing-deals)

```javascript
print agileCRM("opportunity?page_size=10&cursor=Cj8SOWoRc35hZ2lsZS1jcm0tY2xvdWRyGAsSC09wcG9ydHVuaXR5GICAgMCV5oEJDKIBCWdoYW5zaHlhbRgAIAA","GET",None,"application/json")
```

#### 3.5 Get deal by ID


```javascript
print agileCRM("opportunity/5733975435771904","GET",None,"application/json")
```

#### 3.6 Delete deal by ID


```javascript
print agileCRM("opportunity/5733975435771904","DELETE",None,"application/json")
```

## 4. Note
#### 4.1 Create a note and relate that to contacts

```javascript
note_data = {
    "subject": " Note subject",
    "description": "Note description",
    "contact_ids": [
        "5707143030243328",
        "5721389839417344"
    ]
}

print agileCRM("notes","POST",note_data,"application/json")

```

#### 4.2 Add note to a contact using email ID

```javascript
WIP
```

#### 4.3 Gets notes related to specific contact

```javascript
print agileCRM("contacts/5688267051630592/notes","GET",None,"application/json")
```

#### 4.4 Delete a specific note from specific contact

```javascript
print agileCRM("contacts/5688267051630592/notes/5688267051630600","DELETE",None,"application/json")
```

#### 4.5 Create note to a deal

```javascript
note_deal_data = {
    "subject": "Deal From Albany",
    "description": "This deal came directly from customer. No advertisement and hence very important for us.",
    "deal_ids": [
        "5178487182721024"
    ]
}

print agileCRM("opportunity/deals/notes","POST",note_deal_data,"application/json")
```

#### 4.6 Update note to a deal

```javascript
update_note_deal_data = {
    "id": "5714548224950272",
    "subject": "Deal From Albany edit",
    "description": "This deal came directly from customer. No advertisement and hence very important for us.",
    "deal_ids": [
        "5088304026353664"
    ]
}

print agileCRM("opportunity/deals/notes","PUT",update_note_deal_data,"application/json")
```

#### 4.7 Gets notes related to specific deal

```javascript
print agileCRM("opportunity/5728337217454080/notes","GET",None,"application/json")
```

