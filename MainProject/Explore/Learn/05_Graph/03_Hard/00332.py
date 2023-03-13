# Hard 332. Reconstruct Itinerary - маршрут
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight.
# Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

class Solution:
    def findItinerary(self, tickets):
        # tickets: List[List[str]], return List[str]
        self.create_ticket_graph(tickets)
        self.min_route = None
        start_arp = 'JFK'
        self.curr_route = [start_arp]
        for curr_arp in self.ticket_graph[start_arp]['children']: self.proc_node(curr_arp)
        return self.min_route

    def proc_node(self, curr_arp):
        curr_ind = len(self.curr_route)
        if self.min_route is not None and self.min_route[curr_ind] < curr_arp: return

        prev_arp = self.curr_route[-1]
        self.curr_route.append(curr_arp)
        self.ticket_graph[prev_arp]['edges'][curr_arp] -= 1

        if len(tickets) == len(self.curr_route) - 1:
            self.min_route = [arp for arp in self.curr_route]
        elif curr_arp in self.ticket_graph:
            for next_arp in self.ticket_graph[curr_arp]['children']:
                cnt = self.ticket_graph[curr_arp]['edges'][next_arp]
                if cnt == 0: continue
                self.proc_node(next_arp)

        self.curr_route.pop()
        self.ticket_graph[prev_arp]['edges'][curr_arp] += 1

    def create_ticket_graph(self, tickets):
        self.ticket_graph = {}
        for t in tickets:
            src, dst = t[0], t[1]
            if src not in self.ticket_graph: self.ticket_graph[src] = dict(edges={})
            edges = self.ticket_graph[src]['edges']
            if dst not in edges: edges[dst] = 1
            else: edges[dst] += 1
        for item in self.ticket_graph.values():
            item['children'] = sorted(item['edges'].keys())

########## TEST ########################################################################################################
sln = Solution()
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(sln.findItinerary(tickets))
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(sln.findItinerary(tickets))
tickets = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
print(sln.findItinerary(tickets))