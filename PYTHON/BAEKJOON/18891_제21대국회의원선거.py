from functools import reduce


class Party:
    def __init__(self, party_count, vote_count):
        self.party_count = party_count
        self.vote_count = vote_count
        self.is_representative = True

P, V = list(map(int, input().split()))
congress_total, local_congress_total, representative_total = 300, 253, 47
local_party_congress, no_party_congress = 0, 0
available_vote_count = 0

party_dict = {}
for _ in range(P):
    party_name, local_field_count, number_of_votes = list(map(int, input().split()))
    party_dict[party_name] = Party(local_field_count, number_of_votes)
    available_vote_count += number_of_votes
    local_party_congress += local_congress_total
    
no_party_congress = local_congress_total - local_party_congress

    
