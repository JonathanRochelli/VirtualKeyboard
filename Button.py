class Button():
    def __init__(self, pos, text, size, color = (255, 255, 255), opacity=0.6):
        self.pos = pos
        self.text = text
        self.size = size
        self.color = color
        self.opacity = opacity

    def draw(self, img):
        x, y = self.pos
        w, h = self.size
        overlay = img.copy()
        cv2.rectangle(overlay, self.pos, [x + w, y + h], self.color , cv2.FILLED)
        cv2.putText(overlay, self.text, [x + 25, y + 50 ], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
        cv2.addWeighted(overlay, self.opacity, img, 1 - self.opacity, 0, img)
    
    def focus(self):
        self.color = (255, 255, 255)
        self.opacity = 1
    
    def unfocus(self):
        self.color = (255, 255, 255)
        self.opacity = 0.6

    def setColor(self, color):
        self.color = color

    def getText(self):
        return self.text