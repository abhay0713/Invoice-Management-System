from dbcon import mycon
import function

ob1=function.master()


print()
print("\t\t\t\t\tWelcome To Electronic Invoice system")
print("\t\t\t\t\t====================================")
print()
print("\t\t\tFor Master Press---> M | For Invoice Press---> I | For View & Print---> V")
print("\t\t\t=========================================================================")
print()
ch=input("\t\tEnter Your Choice:")
print()

if (ch=="M"):
	print("\t\t\t\t\t\tWelcome To Master Page")
	print("\t\t\t\t\t\t======================")
	print()
	print("\t\t\tFor Category Press---> T | For Brand Press---> B | For Client Press---> C")
	print("\t\t\t=========================================================================")
	print()
	ch1=input("\t\tEnter Your Choice:")
	print()

	if (ch1=="T"):
		print("\t\t\t\t\t\t? Category Management ?")
		print("\t\t\t\t\t\t=======================")
		print()
		print("\t\t\t\tFor Add New Category Press---> N | For Delete Category Press---> D")
		print("\t\t\t\t==================================================================")
		print()
		ch2=input("\t\tEnter Your Choice: ")
		print()

		if (ch2=="N"):
			cat=input("\t\t\tEnter New Category: ")
			ob1.RecordAdd(cat)

		elif (ch2=="D"):
			ob1.RecordDis()
			print()
			dele=input("\t\t\tEnter Cat_ID to Delete Category: ")
			ob1.RecordDel(dele)


	elif (ch1=="B"):
		print()
		print("\t\t\t\t\t\t? Brand Management ?")
		print("\t\t\t\t\t\t====================")
		print()
		print("\t\t\t\tFor Add New Brand Press---> A | For Delete Brand Press---> D")
		print("\t\t\t\t=============================================================")
		print()
		ch=input("\t\tEnter Your Choice: ")
		print()

		if (ch=="A"):
			br=input("\t\t\tEnter New Brand: ")
			ob1.BrandAdd(br)

		elif (ch=="D"):
			ob1.DisplayBrand()
			print()
			dele=input("\t\t\tEnter Brand_id to Delete Brand: ")
			ob1.BrandDel(dele)


	elif(ch1=="C"):
		print()
		print("\t\t\t\t\t\t? Client Management ?")
		print("\t\t\t\t\t\t=====================")
		print()
		print("\t\t\t\tFor Add New Client Press---> A | For Delete Client Press---> D")
		print("\t\t\t\t=============================================================")
		print()
		ch=input("\t\tEnter Your Choice: ")

		if (ch=="A"):
			print()
			name=input("\t\tEnter Client Name: ")
			address=input("\t\tEnter Client Address: ")
			state=input("\t\tEnter Client State: ")
			city=input("\t\tEnter Client City: ")
			cper=input("\t\tEnter Contact Person Name: ")
			mobile=input("\t\tEnter Client Mobile No: ")
			email=input("\t\tEnter Client Mail ID: ")
			gstin=input("\t\tEnter Client GSTIN No: ")
			ob1.ClientAdd(name,address,state,city,cper,mobile,email,gstin)

		elif (ch=="D"):
			ob1.DisplayClient()
			print()
			dele=input("\t\t\tEnter Cust_id to Delete Client: ")
			ob1.ClientDel(dele)


elif (ch=="I"):
	print("\t\t\t\t\t\t? Welcome To Invoice Management ?")
	print("\t\t\t\t\t\t=================================")
	print()
	print("\t\t\tClient Details")
	print("\t\t\t==============")
	print()
	ob1.DisplayClient()
	print()
	print("\t\t\tBrand Details")
	print("\t\t\t=============")
	ob1.DisplayBrand()
	print()
	print("\t\t\tProduct Details")
	print("\t\t\t===============")
	ob1.RecordDis()
	print()
	print("\t\t\t? Please Enter Detials to Generate Bill of Client ?")
	print("\t\t\t===================================================")
	print()
	client_id=input("\t\tEnter Client ID: ")
	brand_id=input("\t\tEnter Brand ID: ")
	product_id=input("\t\tEnter Product ID: ")
	qty=int(input("\t\tEnter Quantity: "))
	rate=int(input("\t\tEnter Rate of Product: "))
	tot=qty*rate
	cgst=tot*9/100
	igst=tot*9/100
	gst=cgst+igst
	total=tot+gst
	ob1.billcalculate(client_id,brand_id,product_id,qty,rate,cgst,igst,gst,total)

elif (ch=="V"):
	print("\t\t\t\t\t\t? Welcome To View Client Invoice ?")
	print("\t\t\t\t\t\t=================================")
	print()
	ob1.customerbilldisplay()
	print()
	billid=input("\t\tPlease Enter Bill_ID to Generate Bill: ")
	print()
	ob1.customerbill(billid)

else:
	print("\t\t$ INVALID CHOICE PLEASE CHOOSE CORRECT OPTION $")
	print("\t\t===============================================")

 

	

      