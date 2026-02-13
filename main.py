#!/usr/bin/env python3
# Lab 06: Inheritance with Classes

# Superclass for Contacts
class Contact:
    contact_list = []
    def __init__(self, name_first, name_last):
        self.name_first = name_first.strip()
        self.name_last = name_last.strip()
    
    def get_name_first(self):
        return self.name_first
    
    def set_name_first(self, value):
        self.name_first = value.strip()
    
    def get_name_last(self):
        return self.name_last
    
    def set_name_last(self, value):
        self.name_last = value.strip()

# Subclass for Emails
class ContactEmail(Contact):
    def __init__(self, name_first, name_last, email):
        Contact.__init__(self, name_first, name_last)
        email = email.strip()
        
        if self.validate(email)==False:
            raise ValueError()
        
        self.email = email
        Contact.contact_list.append(self)
    
    def validate(self, email):
        email = email.strip()
        if "@" in email and (email[-4:]==".com" or email[-4:]==".net"):
            return True
        else:
            return False
    
    def set_info(self, value):
        value = value.strip()
        if self.validate(value)==True:
            self.email = value
        else:
            raise ValueError()

    def get_info(self):
        return self.email
        

# Subclass for Phone Numbers
class ContactPhone(Contact):
    def __init__(self, name_first, name_last, phone):
        Contact.__init__(self, name_first, name_last)
        phone = phone.strip()
        if self.validate(phone)==False:
            raise ValueError()
        self.phone = phone
        Contact.contact_list.append(self)
    
    def validate(self, phone):
        phone = phone.strip()
        phone_format = phone.split("-")
        if (len(phone_format[0])==3) and (len(phone_format[1])==3) and (len(phone_format[2])==4):
            return True
        else:
            return False
        
    def set_info(self, value):
        value = value.strip()
        if self.validate(value):
            self.phone = value

        else:
            raise ValueError()
    
    def get_info(self):
        return self.phone