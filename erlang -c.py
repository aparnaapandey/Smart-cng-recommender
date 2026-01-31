import math

def erlang_c_wait_time(arrival_rate, service_time, servers):
    """
    arrival_rate: vehicles per hour (λ)
    service_time: average service time in minutes
    servers: number of dispensers
    """

    mu = 60 / service_time          # service rate per hour
    lam = arrival_rate              # arrival rate per hour
    c = servers

    rho = lam / (c * mu)

    if rho >= 1:
        return float("inf"), float("inf")

    # Calculate Erlang-C probability
    sum_terms = sum((lam/mu)**n / math.factorial(n) for n in range(c))
    last_term = ((lam/mu)**c / math.factorial(c)) * (c * mu) / (c * mu - lam)

    p_wait = last_term / (sum_terms + last_term)

    # Waiting time in queue (hours)
    Wq = p_wait / (c * mu - lam)

    # Convert to minutes
    Wq_min = Wq * 60
    W_total = Wq_min + service_time

    return Wq_min, W_total
