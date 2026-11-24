
class Square {

    public static void main(String[] args) {
        int r = 100;
        int r1 = 0;
        while (true) {

            for (int y = 1; y <= 2 * r; y++) {

                for (int x = 1; x <= 2 * r; x++) {
                    int k = x * x + y * y
                            + r * r - 2 * r * (x + y);
                    int l = x * x + y * y + 2
                            * r * r - 2 * r * (x + y)
                            - r1 * r1;

                    if (k <= 0 && l >= 0) {
                        System.out.print("***");
                    } else {
                        System.out.print("   ");
                    }

                }
                System.out.println();
            }
            r1 = r1 + 20;
            System.out.print("\u001b[H");
        }
    }
}
