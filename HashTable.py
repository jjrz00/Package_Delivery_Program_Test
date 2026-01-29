from Package import Package

#create HashTable class
class HashTable:

    #create HashTable constructor
    def __init__(self, size=10):
        #store num of buckets
        self.size = size
        #create a list of lists
        self.table = [[] for _ in range(self.size)]

    #create method to insert package into hashtable
    def insert(self, package):
        key = package.package_id
        index = key % 10
        for existing_package in self.table[index]:
            if existing_package.package_id == package.package_id:
                self.table[index].append(existing_package)
                return
        self.table[index].append(package)

    #create lookup method to search for package id in hashtable, if package id not in table, return string
    def lookup(self, package_id):
        key = package_id % 10
        bucket = self.table[key]
        for package in bucket:
            if package.package_id == package_id:
                return package

        return print(f"package_id {package_id} not in table :o")
        return None

    #create string representation method for HashTable instances for when using debugger
    def __repr__ (self):
        result = ""
        for i, bucket in enumerate(self.table):
            if bucket:
                bucket_contents = ", ".join(str(pkg) for pkg in bucket)
            else:
                bucket_contents = "empty :("
            result += f"Bucket {i}: \n {bucket_contents}\n"
        return result

#create string representation method for HashTable instances
def __str__(self):
    result = ""
    for i, bucket in enumerate(self.table):
        if bucket:
            bucket_contents = ", ".join(str(pkg) for pkg in bucket)
        else:
            bucket_contents = "empty :("
        result += f"Bucket {i}: \n {bucket_contents}\n"
    return result
