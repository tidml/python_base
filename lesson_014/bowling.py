from operator import itemgetter
from random import randint


class NotEnoughFrames(Exception):
    pass


class TooManyFrames(Exception):
    pass


class StrikeError(Exception):
    pass


class BowlingGame:

    def __init__(self):
        self.game = []
        self.frame_count = 1
        self.total_points = 0

    def run(self):
        self.frames_results()
        self.scoring()
        self.show_results()

    def frames_results(self):
        while self.frame_count <= 10:
            skittle = 10
            throw_count = 1
            frame = []
            while throw_count <= 2:
                throw = randint(0, skittle)
                if throw == 10:
                    frame.append('X')
                    break
                elif sum(frame) < 10:
                    if sum(frame) + throw == 10:
                        frame.append('/')
                    else:
                        frame.append(throw)
                        skittle -= sum(frame)
                throw_count += 1
            self.game.append(frame)
            self.frame_count += 1

    def scoring(self):
        for index, points in enumerate(self.game):
            if 'X' in points:
                self.total_points += 20
            elif points[1] == '/':
                self.total_points += 15
            else:
                self.total_points += sum(points)

    def show_results(self):
        for frame in self.game:
            if 0 in frame:
                while 0 in frame:
                    i = frame.index(0)
                    frame.remove(0)
                    frame.insert(i, '-')
            print(*frame, sep='', end='')
        print(f' - {self.total_points}')


class BowlingGameWorld(BowlingGame):

    def __init__(self):
        super().__init__()
        self.frame_points = {}

    def run(self):
        self.frames_results()
        self.collecting_frames_points()
        self.scoring()
        self.show_results()

    def collecting_frames_points(self):
        for index, points in enumerate(self.game):
            if 'X' in points:
                self.frame_points[index] = ('X', 10)
            elif points[1] == '/':
                self.frame_points[index] = ('/', 10)
            else:
                self.frame_points[index] = ('S', sum(points))

    def scoring(self):
        for index, frame in enumerate(self.game):
            if '/' in frame or 'X' in frame:
                if index == 9:
                    self.total_points += 10
                    break
                next_frame = self.game[index + 1]
                current_frame_point = 10
                if 'X' in frame:
                    if 'X' in next_frame or '/' in next_frame:
                        next_frame_point = 10
                    else:
                        next_frame_point = sum(next_frame)
                elif '/' in frame:
                    if 'X' in next_frame:
                        next_frame_point = 10
                    else:
                        next_frame_point = next_frame[0]
                self.total_points += current_frame_point + next_frame_point
            else:
                self.total_points += sum(frame)


class BowlingScore(BowlingGame):

    def __init__(self, result):
        super().__init__()
        self.result = result

    def run(self):
        self.get_score()
        try:
            self.check_data()
        except (ValueError, NotEnoughFrames, StrikeError, TooManyFrames) as exc:
            # print(f'Ошибка! {exc}')
            return exc.__class__
        self.scoring()
        self.show_results()
        return self.total_points

    def check_data(self):
        if len(self.game) < 10:
            raise NotEnoughFrames(f'Недостаточно фреймов, необходимо 10, получено {len(self.game)}')
        if len(self.game) > 10:
            raise TooManyFrames(f'Слишком много фреймов, необходимо 10, получено {len(self.game)}')
        if '0' in self.result:
            raise ValueError('Должен быть символ "-", вместо 0 в результатах фрейма')
        if 'X' in self.result:
            symbols_in_game = []
            for frame in self.game:
                for throw in frame:
                    symbols_in_game.append(throw)
            if len(self.result) != len(symbols_in_game):
                raise StrikeError('Strike не может быть 2-м в фрейме, если первы бросок сбил хотя бы 1 кеглю')
        for frame in self.game:
            if len(frame) == 2:
                if frame[0] == '/':
                    raise ValueError('Символ "/" закрывает фрейм и не может стоять в начале')
                elif frame[1] != '/':
                    if sum(frame) == 10:
                        raise ValueError(f'Необхоим символ "/", вместо {frame[1]}, т.к. 2-м броском были выбиты '
                                         f'оставшиеся кегли')

    def get_score(self):
        throws = []
        frame = []
        for index, symbol in enumerate(self.result):
            if symbol.isdigit():
                symbol = int(symbol)
            if symbol == '-':
                throws.append(0)
            else:
                throws.append(symbol)
        for index, symbol in enumerate(throws):
            if symbol == 'X':
                pr_symbol = throws[index - 1]
                if pr_symbol != '-':
                    self.game.append(symbol)
                    continue
            frame.append(symbol)
            if len(frame) == 2:
                self.game.append(frame)
                frame = []

    def show_results(self):
        print(f'{self.result} - {self.total_points}')


class BowlingScoreWorld(BowlingScore, BowlingGameWorld):

    def __init__(self, result):
        BowlingGameWorld.__init__(self)
        BowlingScore.__init__(self, result)

    def run(self):
        BowlingScore.get_score(self)
        try:
            BowlingScore.check_data(self)
        except (ValueError, NotEnoughFrames, StrikeError, TooManyFrames) as exc:
            return exc.__class__
        BowlingGameWorld.collecting_frames_points(self)
        BowlingGameWorld.scoring(self)
        BowlingScore.show_results(self)
        return self.total_points


if __name__ == '__main__':
    game = BowlingScore('42174/34723/X21X33')
    game.run()

    game = BowlingScore('46174/34723/X21X33')
    game.run()

    game = BowlingScore('06174/34723/X21X33')
    game.run()

    game = BowlingScore('174/34723/X21X33')
    game.run()

    game = BowlingScore('/6174/34723/X21X33')
    game.run()

    game = BowlingScore('1X174/34723/X21X33')
    game.run()


class CalculatePlayerResults:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.the_calculated_results_of_the_games = {}
        self.winners = {}

    def run(self):
        self.calculate_results()
        self.write_calculated_results()
        self.show_winners()

    def engine_of_calculate_points(self, result):
        score = BowlingScore(result)
        return score

    def calculate_results(self):
        with open(self.input_file, 'r', encoding='utf8') as file:
            for line in file:
                if len(line[:-1]) == 0:
                    continue
                elif '###' in line or 'is' in line:
                    if '###' in line:
                        i = line[9:-1]
                        self.the_calculated_results_of_the_games[i] = {}
                else:
                    data = line.split('\t')
                    name = data[0]
                    result = data[1][:-1]
                    score = self.engine_of_calculate_points(result)
                    total_point = score.run()
                    self.the_calculated_results_of_the_games[i][f'{name} {result}'] = total_point
                    # if str(total_point).isdigit():
                    # self.the_calculated_results_of_the_games[i][f'{name} {result}'] = total_point

    def write_calculated_results(self):
        with open(self.output_file, 'a', encoding='utf8') as file:
            for game, result in self.the_calculated_results_of_the_games.items():
                file.write(f'### tour {game}\n')
                for player, total_point in result.items():
                    if str(total_point).isdigit():
                        file.write(f'{player} - {total_point}\n')
                    else:
                        file.write(f'{total_point}\n')
                        result[player] = 0
                sorted_result = sorted(result.items(), key=itemgetter(1), reverse=True)
                winner = sorted_result[0][0].split(' ')
                name = winner[0]
                if name in self.winners:
                    self.winners[name] += 1
                else:
                    self.winners[name] = 1
                file.write(f'Winner is {name} - {sorted_result[0][1]}\n\n')

    def show_winners(self):
        sorted_winners_list = sorted(self.winners.items(), key=itemgetter(1), reverse=True)
        print(f'| {"Игрок":^8} | {"Побед":^8} |')
        for winners in sorted_winners_list:
            print(f'+{"+":-^21}+')
            winner, games = winners[0], winners[1]
            print(f'| {winner:^8} | {games:^8} |')


class CalculatePlayerResultsWorld(CalculatePlayerResults):

    def engine_of_calculate_points(self, result):
        score = BowlingScoreWorld(result)
        return score
