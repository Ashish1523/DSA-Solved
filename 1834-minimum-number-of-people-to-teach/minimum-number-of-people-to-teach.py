class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        sad_users=set()

        for u,v in friendships:
            u-=1
            v-=1
            lang_set=set(languages[u])

            can_talk=any(lang in lang_set for lang in languages[v])
            if not can_talk:
                sad_users.add(u)
                sad_users.add(v)
        
        language_count=[0]*(n+1)
        most_known_lang=0

        for user in sad_users:
            for lang in languages[user]:
                language_count[lang]+=1
                most_known_lang=max(most_known_lang,language_count[lang])
        return len(sad_users)-most_known_lang