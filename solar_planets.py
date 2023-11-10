import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20, 250),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Mercury",
            (110, 250),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Venus",
            (187, 175),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.6,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Earth",
            (280, 270),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.8,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Mars",
            (380, 270),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.8,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Jupiter",
            (480, 170),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Saturn",
            (710, 270),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.8,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Uranus",
            (960, 140),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.8,
            (255,0,255),
            2
            )

cv2.putText(img,
            "Neptune",
            (1120, 290),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.8,
            (255,0,255),
            2
            )

cv2.imshow("output", img)

cv2.waitKey(0)

