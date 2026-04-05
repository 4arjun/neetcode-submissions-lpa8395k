class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.heap = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        heapq.heappush(self.heap, (-self.time, userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        temp = []
        self.following[userId].add(userId)
        while self.heap:
            time, user, tweet = heapq.heappop(self.heap)
            if user in self.following[userId]:
                feed.append(tweet)
            temp.append((time, user, tweet))
            if len(feed) == 10:
                break
        for item in temp:
            heapq.heappush(self.heap, item)
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
