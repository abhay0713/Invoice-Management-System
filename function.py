from dbcon import mycon

class master(mycon):
	def RecordAdd(self,name):
		self.name=name
		sql="insert into category(name) values(%s)"
		value=[self.name]
		self.mycursor.execute(sql,value)
		self.mydb.commit()
		print()
		print("\t\t\t ? Category Added Successfully ?")


	def BrandAdd(self,name):
		self.name=name
		sql="insert into brand(brand_name) values(%s)"
		value=[self.name]
		self.mycursor.execute(sql,value)
		self.mydb.commit()
		print()
		print("\t\t\t ? Brand Added Successfully ?")


	def RecordDis(self):
		self.mycursor.execute("select * from category")
		data=self.mycursor.fetchall()
		for i in data:
			print("\t\t",i)

	def DisplayBrand(self):
		self.mycursor.execute("select * from brand")
		data=self.mycursor.fetchall()
		for i in data:
			print("\t\t",i)

	def DisplayClient(self):
		self.mycursor.execute("select cust_id,name,state,city,gstin_no from customer")
		data=self.mycursor.fetchall()
		for i in data:
			print("\t\t",i)

	def RecordDel(self,ide):
		self.ide=ide 
		sql="delete from category where cat_id = %s"
		value=[self.ide]
		self.mycursor.execute(sql,value)
		self.mydb.commit()
		print()
		print("\t\t\t ? Category Deleted Successfully ?")

	def BrandDel(self,ide):
		self.ide=ide 
		sql="delete from brand where brand_id = %s"
		value=[self.ide]
		self.mycursor.execute(sql,value)
		self.mydb.commit()
		print()
		print("\t\t\t ? Brand Deleted Successfully ?")

	def ClientDel(self,ide ):
		self.ide=ide 
		sql="delete from customer where cust_id = %s"
		value=[self.ide]
		self.mycursor.execute(sql,value)
		self.mydb.commit()
		print()
		print("\t\t\t ? Client Deleted Successfully ?")

	def ClientAdd(self,name,address,state,city,cper,mobile,email,gstin):
		self.name=name
		self.address=address
		self.state=state
		self.city=city
		self.cper=cper
		self.mobile=mobile
		self.email=email
		self.gstin=gstin
		sql="insert into customer(name,address,state,city,contact_person,mobile_no,email,gstin_no) values(%s,%s,%s,%s,%s,%s,%s,%s)"
		value=[self.name,self.address,self.state,self.city,self.cper,self.mobile,self.email,self.gstin]
		self.mycursor.execute(sql,value)
		self.mydb.commit()
		print()
		print("\t\t\t ? New Client Added Successfully ?")

	def billcalculate(self,cid,bid,pid,qty,rate,cgst,igst,gst,total):
		self.cid=cid
		self.bid=bid
		self.pid=pid
		self.qty=qty
		self.rate=rate
		self.cgst=cgst
		self.igst=igst
		self.gst=gst
		self.total=total
		sql="insert into bill(cust_id,brand_id,cat_id,qty,rate,cgst,igst,gst,total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		value=[self.cid,self.bid,self.pid,self.qty,self.rate,self.cgst,self.igst,self.gst,self.total]
		self.mycursor.execute(sql,value)
		self.mydb.commit()
		print()
		print("\t\t? Client Bill Successfully Generated ?")

	def customerbilldisplay(self):
		sql="select * from bill"
		self.mycursor.execute(sql)
		data=self.mycursor.fetchall()
		for i in data:
			custid=i[1]
			brandid=i[2]
			proid=i[3]
			sql1="select name from customer where cust_id="+str(custid)
			sql2="select brand_name from brand where brand_id="+str(brandid)
			sql3="select name from category where cat_id="+str(proid)
			self.mycursor.execute(sql1)
			clientname=self.mycursor.fetchall()
			self.mycursor.execute(sql2)
			brandname=self.mycursor.fetchall()
			self.mycursor.execute(sql3)
			productname=self.mycursor.fetchall()
			print("\t",i[0],clientname,productname,brandname,"Quantity:",i[4],"Rate:",i[5],i[6],i[7],"Total:",i[8])


	def customerbill(self,billid):
		self.billid=billid
		sql="select * from bill where bill_id="+str(self.billid)
		self.mycursor.execute(sql)
		data=self.mycursor.fetchall()
		for i in data:
			custid=i[1]
			brandid=i[2]
			proid=i[3]
			sql1="select name from customer where cust_id="+str(custid)
			sql2="select brand_name from brand where brand_id="+str(brandid)
			sql3="select name from category where cat_id="+str(proid)
			self.mycursor.execute(sql1)
			clientname=self.mycursor.fetchall()
			self.mycursor.execute(sql2)
			brandname=self.mycursor.fetchall()
			self.mycursor.execute(sql3)
			productname=self.mycursor.fetchall()
			print("\t\t\t\t? INVOICE DETAILS ?")
			print("\t\t\t\t==================")
			print()
			print("\tInvoice No: ",i[0],"\t\t\t\tClient Name:",clientname)
			print("\tProduct Name:",productname,"\tBrand:",brandname)
			print("\tQuantity: ",i[4],"\t\t\t\tRate: ",i[5])
			print("\tCGST: ",i[6],"IGST: ",i[7],"\tGST: ",i[8])
			print()
			print("\t\t\t\t\t\tTotal Amount: ",i[9])
			print()
			print("\t\t\t$ Thankyou For Shopping $","\t\t& Visit Again &")
			print("\t\t\t=========================","\t\t===============")



