from influxdb import InfluxDBClient
import random

client = InfluxDBClient("ec2-52-14-199-211.us-east-2.compute.amazonaws.com",8086,"","","sensor_measures")

for i in range(1,13):
    for j in range(1,29):
        print("Day: {} Month: {}".format(j,i))
        
        json_body = [
            {
                "measurement": "metrics",
                "tags": {
                    "user": "jamal",
                    "region": "sapucaia"
                },
                "time": "2019-{}-{}T23:00:00Z".format(i,j),
                "fields": {
                    "voltage": random.randint(200,221),
                    "current": random.randint(0,15),
                    "flow": random.randint(0,7)
                }
            }
        ]
        print("Saving into InfluxDB")
        client.write_points(json_body)
