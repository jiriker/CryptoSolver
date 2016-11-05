import urllib
import urllib3
import tokenizer

ct="MLDMSKBKDNNHTSVSMIUTQTMSURKSNMXNBTALIDDQNKLSZKATONLNRSLVEDSNKTJJLSHBMHCDBNNKQJDLKTRKLDJKLKJESKCVMNHJBOKKTTDNNTDMLNQKVDKJSLLRQMSTLSLMTKDBSSETEJSNYNNKJDIKKDTQUJRMKSDQCHQYMRLNNUQNDBNVDJSMKSTEKKQTDLLKNFQMCSSDLKNKLTSSQJMUMZTMQCBMONTKTMNDDTLBLVLLNMTCCZSNQUNMQRSDDMSQDKLJKCDINEGDMKKMBDDIMXRKSDLN"

import urllib
import urllib3
import requests
url = 'https://www.guballa.de/substitution-solver'

# """
# POST
# UTF-8
# English

# """
# import requests

data={
 	'cipher' : 'MLDMSKBKDNNHTSVSMIUTQTMSURKSNMXNBTALIDDQNKLSZKATONLNRSLVEDSNKTJJLSHBMHCDBNNKQJDLKTRKLDJKLKJESKCVMNHJBOKKTTDNNTDMLNQKVDKJSLLRQMSTLSLMTKDBSSETEJSNYNNKJDIKKDTQUJRMKSDQCHQYMRLNNUQNDBNVDJSMKSTEKKQTDLLKNFQMCSSDLKNKLTSSQJMUMZTMQCBMONTKTMNDDTLBLVLLNMTCCZSNQUNMQRSDDMSQDKLJKCDINEGDMKKMBDDIMXRKSDLN',
 	'lang' : 'en',
 	'submit' : 'break' 
    }
r = requests.post(url,data=data)
 
print(r.text)
print(r.json)

# import re
# from mechanize import Browser

# br = Browser()
# br.open('https://www.guballa.de/substitution-solver')
# br.select_form(name="breaker")
# # Browser passes through unknown attributes (including methods)
# # to the selected HTMLForm (from ClientForm).
# br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
# response = br.submit()  # submit current form