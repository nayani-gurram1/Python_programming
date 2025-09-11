day1 = ["Alice@example.com", "bob@example.com", "charlie@example.com", "alice@example.com"]
day2 = ["BOB@example.com", "dave@example.com", "alice@example.com"]
day3 = ["eve@example.com", "alice@example.com", "bob@example.com", "dave@example.com"]
day1_set = set(email.lower() for email in day1)
day2_set = set(email.lower() for email in day2)
day3_set = set(email.lower() for email in day3)
all_attendees = day1_set | day2_set | day3_set
all_three = day1_set & day2_set & day3_set
exactly_one = (day1_set - day2_set - day3_set) | \
              (day2_set - day1_set - day3_set) | \
              (day3_set - day1_set - day2_set)
day1_day2 = day1_set & day2_set
day2_day3 = day2_set & day3_set
day1_day3 = day1_set & day3_set
print("\n========== FINAL ATTENDEE REPORT ==========\n")
print(f"Total unique attendees: {len(all_attendees)}")
print("List of all unique attendees:", sorted(all_attendees))
print("\n--------------------------------------------\n")
print(f"Attendees who attended all three days ({len(all_three)}):")
print(sorted(all_three))
print("\n--------------------------------------------\n")
print(f"Attendees who attended exactly one day ({len(exactly_one)}):")
print(sorted(exactly_one))
print("\n--------------------------------------------\n")
print("Pairwise overlaps:")
print(f"Day1 & Day2 ({len(day1_day2)}): {sorted(day1_day2)}")
print(f"Day2 & Day3 ({len(day2_day3)}): {sorted(day2_day3)}")
print(f"Day1 & Day3 ({len(day1_day3)}): {sorted(day1_day3)}")
print("\n============================================\n")
