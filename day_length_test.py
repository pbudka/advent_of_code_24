import unittest

from day_length import daysFromEquinox, declination, dayLength, sunRiseSunSet, solarTransit


class DayLengthTest(unittest.TestCase):

    def testDayFromEquinox(self):
        self.assertEqual(297, daysFromEquinox(12, 1, 2003))
        self.assertEqual(334, daysFromEquinox(18, 2, 2003))
        self.assertEqual(354, daysFromEquinox(12, 3, 2003))  # leap year next year
        self.assertEqual(353, daysFromEquinox(12, 3, 2004))
        self.assertEqual(0, daysFromEquinox(21, 3, 2003))
        self.assertEqual(31, daysFromEquinox(21, 4, 2003))
        self.assertEqual(9, daysFromEquinox(30, 3, 2003))
        self.assertEqual(53, daysFromEquinox(13, 5, 2003))
        self.assertEqual(267, daysFromEquinox(13, 12, 2003))

    def ignoredTestDeclination(self):
        self.assertAlmostEqual(-19.31, declination(13, 1, 2003), 2)
        self.assertAlmostEqual(-10.23, declination(12, 2, 2003), 2)
        self.assertAlmostEqual(0, declination(21, 3, 2003), 2)
        self.assertAlmostEqual(-4.51, declination(12, 3, 2003), 2)
        self.assertAlmostEqual(-4.9, declination(12, 3, 2004), 2)
        self.assertAlmostEqual(3.62, declination(30, 3, 2003), 2)
        self.assertAlmostEqual(20.91, declination(13, 5, 2003), 2)
        self.assertAlmostEqual(-8.43, declination(30, 9, 2003), 2)
        self.assertAlmostEqual(-23.39, declination(13, 12, 2003), 2)
        self.assertAlmostEqual(-22.95, declination(21, 12, 2003), 2)

    def ignoredTestDayLength(self):
        lat = {'havirov': 49.76, 'athens': 37.93, 'cape town': -34.05}
        expDayLength = {'havirov': [8.94, 12.17, 12.74, 15.79, 10.83, 8.12],
                        'athens': [10.04, 12.14, 12.52, 14.47, 11.26, 9.54],
                        'cape town': [13.97, 12.13, 11.81, 10.15, 12.9, 14.42]}
        for c, l in lat.items():
            with self.subTest(i=c):
                self.assertAlmostEqual(expDayLength[c][0], dayLength(l, 13, 1, 2003), 2)
                self.assertAlmostEqual(expDayLength[c][1], dayLength(l, 21, 3, 2003), 2)
                self.assertAlmostEqual(expDayLength[c][2], dayLength(l, 30, 3, 2003), 2)
                self.assertAlmostEqual(expDayLength[c][3], dayLength(l, 13, 5, 2003), 2)
                self.assertAlmostEqual(expDayLength[c][4], dayLength(l, 30, 9, 2003), 2)
                self.assertAlmostEqual(expDayLength[c][5], dayLength(l, 13, 12, 2003), 2)

    def testSolarTransit(self):
        long = {'havirov': 18.45, 'athens': 23.74}
        expSolarTransit = {'havirov': [(12, 0), (11, 44), (11, 46), (11, 46), (11, 29), (11, 54)],
                           'athens': [(11, 39), (11, 23), (11, 25), (11, 25), (11, 8), (11, 33)]}
        for c, l in long.items():
            with self.subTest(i=c):
                self.assertEqual(expSolarTransit[c][0], solarTransit(l, 13, 1, 2003))
                self.assertEqual(expSolarTransit[c][1], solarTransit(l, 21, 3, 2003))
                self.assertEqual(expSolarTransit[c][3], solarTransit(l, 13, 5, 2003))
                self.assertEqual(expSolarTransit[c][4], solarTransit(l, 30, 9, 2003))
                self.assertEqual(expSolarTransit[c][5], solarTransit(l, 13, 12, 2003))

    def testSunRiseSunSet(self):
        lat = {'havirov': 49.76, 'athens': 37.93, 'cape town': -34.05}
        # https://www.timeanddate.com/sun/ 7:40    16:10       6:27     19:16       4:52     20:35       6:04     19:27      7:41     15:47
        expSunRiseSunSet = {'havirov': [((7, 44), (16, 15)), ((6, 35), (19, 24)), ((5, 7), (20, 52)), ((6, 22), (19, 37)), ((7, 56), (16, 3))],
            'athens': [((7, 6), (16, 53)), ((6, 42), (19, 17)), ((5, 46), (20, 13)), ((6, 34), (19, 25)), ((7, 13), (16, 46))],
            'cape town': [((4, 53), (19, 6)), ((7, 6), (18, 53)), ((7, 54), (18, 5)), ((7, 13), (18, 46)), ((4, 46), (19, 13))]}
        for c, l in lat.items():
            with self.subTest(i=c):
                self.assertEqual(expSunRiseSunSet[c][0], tuple(sunRiseSunSet(l, 13, 1, 2003)))
                self.assertEqual(expSunRiseSunSet[c][1], tuple(sunRiseSunSet(l, 31, 3, 2003)))
                self.assertEqual(expSunRiseSunSet[c][2], tuple(sunRiseSunSet(l, 23, 5, 2003)))
                self.assertEqual(expSunRiseSunSet[c][3], tuple(sunRiseSunSet(l, 3, 9, 2003)))
                self.assertEqual(expSunRiseSunSet[c][4], tuple(sunRiseSunSet(l, 20, 12, 2003)))


if __name__ == '__main__':
    unittest.main()
