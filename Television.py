class Television:
  def __init__(self):
    self.current_channel = 1
    self.is_on = False
    self.volume = 10

  def set_channel(self, new_channel):
    self.current_channel = new_channel

  def channel_up(self):
    self.current_channel += 1

  def channel_down(self):
    self.current_channel -= 1

  def toggle_on_off(self):
    self.is_on = not self.is_on
  
  def mute(self):
    self.volume = 0

  def volume_up(self):
    self.volume += 1
  
  def volume_down(self):
    self.volume -= 1

my_tv = Television()

print(my_tv.current_channel)
my_tv.channel_up()
print(my_tv.current_channel)
my_tv.set_channel(10)
print(my_tv.current_channel)
