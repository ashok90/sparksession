# Solution to Lab 2.1 if using Pyspark shell
#./bin/Pyspark   to launch the pyspark shell
# print statements added so you den see the value

#To define indexes:
auctionid = 0
bid = 1
bidtime = 2
bidder = 3
bidderrate = 4
openbid = 5
price = 6
itemtype = 7
daystolive = 8

#To load the file
auctionRDD = sc.textFile("/spark/data/input/auctiondata.csv").map(lambda line:line.split(","))

#1. To see the first element of the RDD
auctionRDD.first

# 2. To see the first 5 elements of the RDD
auctionRDD.take(5)

#3. What is the total number of bids?
totbids = auctionRDD.count()
print totbids

#4. What is the total number of distinct items that were auctioned?
totitems = auctionRDD.map(lambda line:line[auctionid]).distinct().count()
print totitems

#5. What is the total number of item types that were auctioned?
totitemtypes=auctionsRDD.map(lambda line:line[itemtype]).distinct().count()
print totitemtypes 

#6. What is the total number of bids per item type?
bids_itemtype = auctionRDD.map(lambda x:(x[itemtype],1)).reduceByKey(lambda x,y:x+y).collect()
print bids_itemtype

#7. What is the total number of bids per auction?
bids_auctionRDD = auctionRDD.map(lambda x:(x[auctionid],1)).reduceByKey(lambda x,y:x+y)
bids_auctionRDD.take(5) #just to see the first 5 elements

#8. Across all auctioned items, what is the max number of bids?
maxbids = bids_auctionRDD.map(lambda x:x[bid]).reduce(max)
print maxbids

#9. Across all auctioned items, what is the minimum of bids?
minbids = bids_auctionRDD.map(lambda x:x[bid]).reduce(min)
print minbids

#10. What is the average bid?
avgbids = totbids/totitems
print avgbids
