#!/usr/bin/python

import sys, string, MySQLdb
from Availability import Avl_Query

def main ():

  selection = 0

  # Initialize database connection
  db=MySQLdb.Connection(host="localhost",user="schedule",
                        passwd="",db="availability")
  db_cursor = db.cursor()

  while selection != "5":
    sub_selection = ""
    # To be replaced with fancy curses interface, says monleezy
    print("\n\n+======================================================+")
    print("|               Welcome, Herder of CATS                |")
    print("|  1) Display All Availability in Weekly View          |")
    print("|  2) Display All Availability for a Specific Day      |")
    print("|  3) Display All Availability for a Specific DeskCAT  |")
    print("|  4) Show DeskCATS Who Haven't Updated Availability   |")
    print("|  5) Exit                                             |")
    print("+======================================================+\n")

    selection = raw_input("Select an Action: ")

    if selection == "\n":
      print("Try again...\n")

    if selection == "1":
      Avl_Query.Display_All_Avail(db_cursor)

    elif selection == "2":
      while sub_selection != "back":
        sub_selection = raw_input("\nView all availability for which day? (\"back\" to return to menu)\n")
        if sub_selection != "back":
          Avl_Query.Display_Day_Avail(sub_selection, db_cursor)

    elif selection == "3":
      while sub_selection != "back":
        sub_selection = raw_input("\nView all availability for which Deskcat? (\"back\" to return to menu)\n")
        if sub_selection != "back":
          Avl_Query.Display_DeskcatAvail_ByDay(sub_selection, db_cursor)

    elif selection == "4":
      Avl_Query.No_Recent_Update(db_cursor)


if __name__ == '__main__':
  main()


