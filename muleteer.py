#!/usr/bin/env python2

import argparse
import math

MULE_CAP_60 = 40.0
MULE_CAP_120 = 20.0
IRON_RATION_PRICE = 3.5
STD_RATION_PRICE = 1.5
STD_RATION_LIFESPAN = 7
IRON_RATION_LIFESPAN = 60

def muleteer(mans:int, days:int):
  # per page 94, 8 lb of water and 2lb of food (1 st total) per man per day
  # rations are sold per week, -> 1.4st of food per price given

  mule_requirements = ""
  if days > IRON_RATION_LIFESPAN:
    mule_requirements += "WARNING: This trip is so long that your iron rations will spoil.  You will need to forage.\n"

  supply_mass = mans*days
  # assum: 1.5gp/man*week for standard rations, 3.5gp/man*week for iron rations
  supply_cost = mans * (STD_RATION_PRICE * min(days, 7) + IRON_RATION_PRICE * max(days-7, 0)) / 7.0
  num_mules_60 = int(math.ceil(supply_mass / MULE_CAP_60))
  num_mules_120 = int(math.ceil(supply_mass / MULE_CAP_120))
  mule_requirements += ("At 60' speed, you will need %d mules to carry rations, and have %0.1f stone extra carrying capacity.\n"%(num_mules_60, num_mules_60 * MULE_CAP_60 - supply_mass))
  mule_requirements += ("At 120' speed, you will need %d mules to carry rations, and have %0.1f stone extra carrying capacity.\n"%(num_mules_120, num_mules_120 * MULE_CAP_120 - supply_mass))
  mule_requirements += ("Your rations for this trip will cost %0.1f gp (%0.1f per person)\n"%(supply_cost, supply_cost / mans))
  return mule_requirements

#def main():
#  parser = argparse.ArgumentParser(description="Compute XP and GP shares for party members")
#  parser.add_argument("-mans",default=10,type=int,help="Number of mans on expedition")
#  parser.add_argument("-days",default=7,type=int,help="Number of days of food to bring")
#  args = parser.parse_args()

#  mans = args.mans
#  days = args.days
#  print (muleteer(mans, days))

#if __name__ == "__main__":
#  main()