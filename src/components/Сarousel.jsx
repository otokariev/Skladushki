import { useEffect } from "react";
import $ from "jquery";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "slick-carousel/slick/slick.js";

function Carousel() {
  useEffect(() => {
    $(".your-carousel-class").slick({
      // Ваши настройки Slick Carousel
      vertical: true,
      swipe: false, // Отключаем свайп по умолчанию
      swipeToSlide: true, // Разрешаем свайп для переключения слайдов
      touchMove: true, // Отключаем свайп по умолчанию на тач-устройствах
      prevArrow: $(".your-prev-button"),
      nextArrow: $(".your-next-button"),
    });
  }, []);
  return (
    <div>
      <button className="your-prev-button">Previous</button>
      <div className="your-carousel-class">
        {/* Ваш контент для слайдов */}
        <div className="carousel__pic">
          <h3>
            <img src="/img/img.jpeg" alt="" />
          </h3>
        </div>
        <div className="carousel__pic">
          <h3>
            <img src="/img/2991974000.jpg" alt="" />
          </h3>
        </div>
        <div className="carousel__pic">
          <h3>
            <img src="/img/2991974000.jpg" alt="" />
          </h3>
        </div>
        {/* Добавьте сколько угодно слайдов */}
      </div>
      <button className="your-next-button">Next</button>
    </div>
  );
}

export default Carousel;
