try:
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.colors import HexColor, Color

    CAN_GENERATE_PDF = True
except ImportError:
    CAN_GENERATE_PDF = False

from core.core import matching as match_func

class PdfGenerator:
    """Генератор PDF отчётов с доминирующими цветами."""

    def __init__(self, font_path=None):
        self.font_path = font_path or 'font/arial.ttf'

    def save_pdf(self, file: str, colors, imgfile: str):

        """Создание PDF файла с отчётом о доминирующих цветах.

        Args:
            file: Путь к выходному PDF файлу
            colors: Список цветов в формате hex (#RRGGBB)
            imgfile: Путь к исходному изображению
        """

        canvas = Canvas(file, pagesize=A4)
        
        pdfmetrics.registerFont(TTFont('Arial', self.font_path))
        
        canvas.setFont('Arial', 16)
        canvas.drawString(20, 800, "Доминирующие цвета")
        
        canvas.setFont('Arial', 12)
        for key, color in enumerate(colors):
            canvas.setFillColor(HexColor('#%s' % color))
            canvas.rect(20, 765 - 30 * key, 70, 25, fill=1, stroke=0)

            # Определение цвета текста (светлый тёмный фон или наоборот)
            matching_color = self._matching(color)
            canvas.setFillColor(HexColor(matching_color))
            canvas.drawCentredString(50, 775 - 30 * key, '#{}'.format(color))

            canvas.drawImage(imgfile, 100, 390, 300, 400, 
                            preserveAspectRatio=True, anchor='nw')

        canvas.save()

    def _matching(self, color):
        """Определение цвета текста для читабельности.

        Args:
            color: Цвет в формате hex (#RRGGBB)

        Returns:
            '#000000' или '#ffffff' в зависимости от яркости цвета
        """
        return match_func(color)
