pool_volume = int(input())
first_pipe_hourly_debit = int(input())
second_pipe_hourly_debit = int(input())
hours_absent = float(input())
first_pipe_total_debit = first_pipe_hourly_debit * hours_absent
second_pipe_total_debit = second_pipe_hourly_debit * hours_absent
total_debit = first_pipe_total_debit + second_pipe_total_debit
percent_filled_first_pipe = first_pipe_total_debit / total_debit * 100
percent_filled_second_pipe = second_pipe_total_debit / total_debit * 100
total_percent_filled = total_debit / pool_volume * 100

if total_percent_filled <= 100:
    print(f"The pool is {total_percent_filled:.2f}% full. Pipe 1: {percent_filled_first_pipe:.2f}%."
          f" Pipe 2: {percent_filled_second_pipe:.2f}%.")
else:
    litres_overflow = total_debit - pool_volume
    print(f"For {hours_absent:.2f} hours the pool overflows with {litres_overflow:.2f} liters.")
