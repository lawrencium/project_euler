__author__ = 'lawrencechen'


# noinspection PyClassHasNoInit
class DiskColor:
    RED = 0
    BLUE = 1


# noinspection PyClassHasNoInit
class DiskGame:
    @staticmethod
    def win_probability(total_rounds, current_round, previously_observed_blue_disks):
        number_blue_disks_to_win = total_rounds / 2 + 1

        total_disks = 2 + current_round - 1
        draw_blue_disk_probability = float(1) / total_disks

        if current_round == total_rounds:
            if previously_observed_blue_disks >= number_blue_disks_to_win:
                return 1
            elif previously_observed_blue_disks + 1 >= number_blue_disks_to_win:
                return draw_blue_disk_probability
            else:
                return 0
        else:
            draw_red_disk_probability = 1 - draw_blue_disk_probability
            win_probability_if_blue_disk_drawn_in_this_round = draw_blue_disk_probability * DiskGame.win_probability(
                total_rounds, current_round + 1, previously_observed_blue_disks + 1)
            win_probability_if_red_disk_drawn_in_this_round = draw_red_disk_probability * DiskGame.win_probability(
                total_rounds, current_round + 1, previously_observed_blue_disks)
            return win_probability_if_blue_disk_drawn_in_this_round + win_probability_if_red_disk_drawn_in_this_round
