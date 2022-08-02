history = ["ICN"]
possible_paths = []

def dfs(airport, used_tickets, ticket_cnt, tickets, n):
    for i in range(n):
        if ((not used_tickets[i]) and (tickets[i][0] == airport)):
            used_tickets[i] = 1
            ticket_cnt += 1
            history.append(tickets[i][1])
            if (ticket_cnt != n):
                dfs(tickets[i][1], used_tickets, ticket_cnt, tickets, n)
            else:
                possible_paths.append(history.copy())
            used_tickets[i] = 0
            ticket_cnt -= 1
            history.pop()
            
def solution(tickets):
    n = len(tickets)
    ticket_cnt = 0
    used_tickets = [0 for i in range(n)]
    dfs("ICN", used_tickets, ticket_cnt, tickets, n)
    
    answer = min(possible_paths)
    return answer