import hashlib


pass_text = "Abc123"
print(hashlib.md5(pass_text.encode('utf-8')).hexdigest())
# 61bd60c60d9fb60cc8fc7767669d40a1
print(hashlib.sha1(pass_text.encode('utf-8')).hexdigest())
# bec75d2e4e2acf4f4ab038144c0d862505e52d07
print(hashlib.sha256(pass_text.encode('utf-8')).hexdigest())
# 7f91e8a4b648b0125b15dc5a3b6466f9f4906d92c72bea9bd6be92c853bebda2
print(hashlib.sha512(pass_text.encode('utf-8')).hexdigest())
# bc30ecc758c63691c69e66d846326670924bff9609b5febf39c1e86cca8fb72783ad5e5b7076359e6d709bc58cd379ade1495945f8591e9876cb2634e43139a6
print(hashlib.sha224(pass_text.encode('utf-8')).hexdigest())
# b66616cbd459ed4bd029482855334a8aee87984287498309e0a1d957
print(hashlib.sha384(pass_text.encode('utf-8')).hexdigest())
# 7d22fc23ffa840c97b1b5385cb82e88e4e419c9c6a0a7ef6edad02537add78a695b2c5c8af4cbeba1cbd66708d6b2b49
