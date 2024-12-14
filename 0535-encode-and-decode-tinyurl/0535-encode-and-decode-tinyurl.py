import random

class Codec:
    urls = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        endpoint = self.generate()
        self.urls[endpoint] = longUrl
        return endpoint
        
    def generate(self) -> str:
        result = ''
        for i in range(6):
            num = chr(random.randrange(ord('0'), ord('9')))
            lower = chr(random.randrange(ord('a'), ord('z')))
            upper = chr(random.randrange(ord('A'), ord('Z')))
            result += random.choice([num,lower,upper])
        
        return result
            

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))