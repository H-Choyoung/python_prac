// 원뿔의 부피 계산하는 애플리케이션

const cone_volume = (radius, height) => {
  if (
    1 <= radius <= 100 &&
    Number.isInteger(radius) === true &&
    1 <= height <= 100 &&
    Number.isInteger(height) === true
  ) {
    const r = radius;
    const h = height;
    const perimeter = 3.14159;

    const result = (perimeter * Math.pow(r, 2) * h) / 3;
    if (typeof result === 'number') {
      return result;
    }
  }
};

console.log(cone_volume(2, 90));
