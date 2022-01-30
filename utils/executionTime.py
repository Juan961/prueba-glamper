from datetime import datetime

def execution_time(func):
  def wrapper(*args, **kwargs):
    initialTime = datetime.now()
    func(*args, **kwargs)
    finalTime = datetime.now()

    timeElapsed = finalTime - initialTime 

    print("Generated in " + str(timeElapsed.total_seconds()) + " seconds")

  return wrapper