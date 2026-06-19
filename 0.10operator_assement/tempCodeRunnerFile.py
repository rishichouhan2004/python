overs=48.3
runs=275
ball=((overs*10)//10)*6
extra_balls=(overs*10)%10
total_balls=int(ball+extra_balls)
print(f"the total balls={total_balls}")
run_rate=runs/total_balls*6
print(f"the run rate={(run_rate)}")
      