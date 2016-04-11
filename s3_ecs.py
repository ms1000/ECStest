import boto
import boto.s3.connection
access_key = '130815670044795073@ecstestdrive.emc.com'
secret_key = 'rJZDp/VD5pH52OMELuQ09sd8KRZuGVpP46m9tPEo'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'object.ecstestdrive.com',
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
#bucket = conn.create_bucket('first_bucket')
for bucket in conn.get_all_buckets():
        print ("{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        ))
mybucket = conn.get_bucket('first_bucket')
#key = mybucket.new_key('test.txt')
#key.set_contents_from_filename('text.txt')
for key in mybucket.list():
   print ("{name}".format(name = key,))
