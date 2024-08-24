import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt

class FootballPlayerAnalysis:
    def __init__(self):
        self.players_data = {}

    def get_int_input(self, prompt):
        while True:
            value = simpledialog.askinteger("Input", prompt)
            if value is not None:
                return value
            else:
                messagebox.showerror("Invalid input", "Please enter an integer value.")

    def get_player_stats(self, num_players):
        players_stats = []
        for i in range(num_players):
            player_name = simpledialog.askstring("Input", f"Enter player {i+1} name: ")
            goals = self.get_int_input(f"Enter goals scored by {player_name}: ")
            assists = self.get_int_input(f"Enter assists made by {player_name}: ")
            time_played = self.get_int_input(f"Enter time played (minutes) by {player_name}: ")
            final_third_passes = self.get_int_input(f"Enter key final third passes by {player_name}: ")
            total_passes = self.get_int_input(f"Enter total passes by {player_name}: ")
            chance_created = self.get_int_input(f"Enter chances created by {player_name}: ")
            successful_dribbles = self.get_int_input(f"Enter successful dribbles by {player_name}: ")
            shots = self.get_int_input(f"Enter shots by {player_name}: ")
            shots_on_target = self.get_int_input(f"Enter shots on target by {player_name}: ")
            freekicks_scored = self.get_int_input(f"Enter freekicks scored by {player_name}: ")
            penalties_scored = self.get_int_input(f"Enter penalties scored by {player_name}: ")
            crosses = self.get_int_input(f"Enter crosses by {player_name}: ")
            ground_duels = self.get_int_input(f"Enter ground duels won (%) by {player_name}: ")
            ariel_duels = self.get_int_input(f"Enter aerial duels won (%) by {player_name}: ")
            interceptions = self.get_int_input(f"Enter interceptions by {player_name}: ")
            tackles = self.get_int_input(f"Enter tackles by {player_name}: ")
            game_changing_tackles = self.get_int_input(f"Enter game-changing tackles by {player_name}: ")
            fouls_won = self.get_int_input(f"Enter fouls won by {player_name}: ")
            yellow_cards = self.get_int_input(f"Enter yellow cards received by {player_name}: ")
            red_cards = self.get_int_input(f"Enter red cards received by {player_name}: ")
            total_saves = self.get_int_input(f"Enter total saves (including penalties) by {player_name}: ")

            player_stats = {
                "name": player_name,
                "goals": goals,
                "assists": assists,
                "time_played": time_played,
                "final_third_passes": final_third_passes,
                "total_passes": total_passes,
                "chance_created": chance_created,
                "successful_dribbles": successful_dribbles,
                "shots": shots,
                "shots_on_target": shots_on_target,
                "freekicks_scored": freekicks_scored,
                "penalties_scored": penalties_scored,
                "crosses": crosses,
                "ground_duels": ground_duels,
                "ariel_duels": ariel_duels,
                "interceptions": interceptions,
                "tackles": tackles,
                "game_changing_tackles": game_changing_tackles,
                "fouls_won": fouls_won,
                "yellow_cards": yellow_cards,
                "red_cards": red_cards,
                "total_saves": total_saves
            }

            player_stats["points"] = self.calculate_points(player_stats)
            players_stats.append(player_stats)
        return players_stats

    def calculate_points(self, stats):
        points = (1500 * stats["goals"] +
                  1000 * stats["assists"] +
                  stats["time_played"] +
                  5 * stats["final_third_passes"] +
                  2 * stats["total_passes"] +
                  150 * stats["chance_created"] +
                  50 * stats["successful_dribbles"] +
                  70 * stats["shots"] +
                  100 * stats["shots_on_target"] +
                  400 * stats["freekicks_scored"] +
                  200 * stats["penalties_scored"] +
                  100 * stats["crosses"] +
                  50 * stats["ground_duels"] +
                  60 * stats["ariel_duels"] +
                  120 * stats["interceptions"] +
                  300 * stats["tackles"] +
                  600 * stats["game_changing_tackles"] +
                  100 * stats["fouls_won"] +
                  -250 * stats["yellow_cards"] +
                  -750 * stats["red_cards"] +
                  1100 * stats["total_saves"])
        return points

    def analyze_match(self):
        match_went_to_penalties = messagebox.askyesno("Input", "Did the match go to penalties?")

        # First team input
        team1_name = simpledialog.askstring("Input", "Enter the first team name: ")
        num_players_team1 = self.get_int_input(f"Enter total players played for {team1_name}: ")
        team1_stats = self.get_player_stats(num_players_team1)
        
        if match_went_to_penalties:
            self.get_penalty_stats(team1_stats)
            self.get_saves_stats(team1_stats)

        # Second team input
        team2_name = simpledialog.askstring("Input", "Enter the second team name: ")
        num_players_team2 = self.get_int_input(f"Enter total players played for {team2_name}: ")
        team2_stats = self.get_player_stats(num_players_team2)

        if match_went_to_penalties:
            self.get_penalty_stats(team2_stats)
            self.get_saves_stats(team2_stats)

        # Process the collected stats to find the best player
        self.determine_best_player(team1_stats, team2_stats)
        self.visualize_points(team1_stats + team2_stats)

    def get_penalty_stats(self, team_stats):
        for player in team_stats:
            if messagebox.askyesno("Input", f"Did {player['name']} take a penalty?"):
                goals = self.get_int_input(f"Enter penalty goals scored by {player['name']}: ")
                misses = self.get_int_input(f"Enter penalties missed by {player['name']}: ")
                player["penalty_goals"] = goals
                player["penalty_misses"] = misses

    def get_saves_stats(self, team_stats):
        for player in team_stats:
            if messagebox.askyesno("Input", f"Did {player['name']} save a penalty?"):
                saves = self.get_int_input(f"Enter penalties saved by {player['name']}: ")
                player["penalty_saves"] = saves

    def determine_best_player(self, team1_stats, team2_stats):
        all_players = team1_stats + team2_stats
        best_player = max(all_players, key=lambda player: player['points'])
        messagebox.showinfo("Best Player", f"The best player on the pitch is {best_player['name']} with {best_player['points']} points")

    def analyze_season(self):
        num_players = self.get_int_input("Enter total number of players in the season: ")
        players_stats = self.get_player_stats(num_players)
        
        # Process the collected season stats to find the man of the tournament
        self.determine_man_of_the_tournament(players_stats)
        self.visualize_points(players_stats)

    def determine_man_of_the_tournament(self, players_stats):
        all_players = []
        for player in players_stats:
            motm = self.get_int_input(f"Enter man of the matches for {player['name']}: ")
            games_played = self.get_int_input(f"Enter games played by {player['name']}: ")
            trophies_won = self.get_int_input(f"Enter trophies won by {player['name']}: ")
            player_of_the_tournament = self.get_int_input(f"Enter player of the tournament awards for {player['name']}: ")
            top_goal_scorer = self.get_int_input(f"Enter top goal scorer awards for {player['name']}: ")
            best_goalkeeper = self.get_int_input(f"Enter best goalkeeper awards for {player['name']}: ")

            player["motm"] = motm
            player["games_played"] = games_played
            player["trophies_won"] = trophies_won
            player["player_of_the_tournament"] = player_of_the_tournament
            player["top_goal_scorer"] = top_goal_scorer
            player["best_goalkeeper"] = best_goalkeeper

            player["points"] += (1000 * motm +
                                 100 * games_played +
                                 7000 * trophies_won +
                                 15000 * player_of_the_tournament +
                                 10000 * top_goal_scorer +
                                 10000 * best_goalkeeper)
            
            all_players.append(player)
        
        man_of_the_tournament = max(all_players, key=lambda player: player['points'])
        messagebox.showinfo("Man of the Tournament", f"The man of the tournament is {man_of_the_tournament['name']} with {man_of_the_tournament['points']} points")

    def visualize_points(self, players):
        names = [player["name"] for player in players]
        points = [player["points"] for player in players]
        
        plt.figure(figsize=(10, 8))
        plt.pie(points, labels=names, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title("Player Points Distribution")
        plt.show()


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Football Player Analysis")
        self.analysis = FootballPlayerAnalysis()

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        self.title_label = tk.Label(self.main_frame, text="Football Player Analysis", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.match_button = tk.Button(self.main_frame, text="Analyze Match", command=self.analyze_match)
        self.match_button.pack(pady=5)

        self.season_button = tk.Button(self.main_frame, text="Analyze Season", command=self.analyze_season)
        self.season_button.pack(pady=5)

    def analyze_match(self):
        self.analysis.analyze_match()

    def analyze_season(self):
        self.analysis.analyze_season()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
