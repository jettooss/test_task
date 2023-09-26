import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    private final Scanner scanner;
    private final Random random;
    private final int lowerBound;
    private final int upperBound;

    public GuessingGame(int lowerBound, int upperBound) {
        this.scanner = new Scanner(System.in);
        this.random = new Random();
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }

    public void play() {
        while (true) {
            int target = generateTarget();
            System.out.printf("Угадай число от %d до %d\n", lowerBound, upperBound);
            boolean guessed = false;
            while (!guessed) {
                int guess = readGuess();
                guessed = checkGuess(target, guess);
            }
            if (!askToContinue()) {
                break;
            }
        }
    }

    private int generateTarget() {
        return random.nextInt(upperBound - lowerBound + 1) + lowerBound;
    }

    private int readGuess() {
        return scanner.nextInt();
    }

    private boolean checkGuess(int target, int guess) {
        if (guess == target) {
            System.out.println("Правильно! (╯°□°)╯");
            return true;
        }
        if (guess < lowerBound || guess > upperBound) {
            System.out.println("Читать не умеешь?");
        } else if (Math.abs(guess - target) > 5) {
            System.out.println("Холодно");
        } else if (Math.abs(guess - target) > 2) {
            System.out.println("Тепло");
        } else {
            System.out.println("Жгётся!");
        }
        return false;
    }

    private boolean askToContinue() {
        System.out.println("Будешь угадывать? (да/нет)");
        while (true) {
            String answer = scanner.next().trim().toLowerCase();
            if (answer.equals("да")) {
                return true;
            } else if (answer.equals("нет")) {
                System.out.println("(¬_¬)");
                return false;
            } else {
                System.out.println("Непонятно, введи да или нет.");
            }
        }
    }

    public static void main(String[] args) {
        GuessingGame game = new GuessingGame(1, 10);
        System.out.println("Привет! Давай угадаем число!");
        game.play();
    }
}
