WITH CombinedRequests AS (
    SELECT requester_id AS user_id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS user_id, requester_id AS friend_id
    FROM RequestAccepted
),
FriendCounts AS (
    SELECT user_id, COUNT(friend_id) AS num_friends
    FROM CombinedRequests
    GROUP BY user_id
),
MaxFriends AS (
    SELECT MAX(num_friends) AS max_friends
    FROM FriendCounts
)
SELECT user_id AS id, num_friends AS num
FROM FriendCounts
WHERE num_friends = (SELECT max_friends FROM MaxFriends);
