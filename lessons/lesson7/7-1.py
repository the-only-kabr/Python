function Complex(real, imagine)
        {
            this.real = real;
            this.imagine = imagine;
            // Сложение
            this.add = cplx2 => new Complex(this.real + cplx2.real, this.imagine + cplx2.imagine);
            // Вычитанлие
            this.def = cplx2 => new Complex(this.real - cplx2.real, this.imagine - cplx2.imagine);
            // Умножение
            this.mult = cplx2 =>
            {
                let [{ real: a, imagine: b }, { real: c, imagine: d }] = [this, cplx2];
                return new Complex(a * c - b * d, b * c + a * d);
            };
            // Деление
            this.dev = cplx2 =>
            {
                let [{ real: a, imagine: b }, { real: c, imagine: d }] = [this, cplx2];
                return new Complex((a * c + b * d) / (c * c + d * d), (a * c - b * d) / (c * c + d * d));
            }
            this.toString = () => `${this.real} ${imagine < 0 ? "-" : "+"} ${Math.abs(this.imagine)}i`;
            return this;
        }
 
 
        let cplx1 = new Complex(3, 5);
        let cplx2 = new Complex(2, 8);
 
        console.log("" + cplx1.add(cplx2));
        console.log("" + cplx1.def(cplx2));
        console.log("" + cplx1.mult(cplx2));
        console.log("" + cplx1.dev(cplx2));
