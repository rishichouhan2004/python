bill=int(input("enter the bill amount="))
gst=int (input("enter the gst amount="))
service_charge=int(input("enter the service charge="))
friends=int(input("enter the friends="))
new_gst=(bill*gst)/100
new_service_charge=(bill*service_charge)/100
final_bill=new_gst+new_service_charge+bill
person_pays=final_bill/friends
print(new_gst)
print(final_bill)
print(person_pays)