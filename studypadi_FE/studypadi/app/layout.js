import localFont from "next/font/local";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

const trocchi = localFont({
  src: "./fonts/Trocchi-Regular.ttf",
  variable: "--font-trocchi",
  weight: "400",
});

const trochutBold = localFont({
  src: "./fonts/Trochut-Bold.ttf",
  variable: "--font-trochut-bold",
  weight: "700",
});

const trochutItalic = localFont({
  src: "./fonts/Trochut-Italic.ttf",
  variable: "--font-trochut-italic",
  weight: "400",
  style: "italic",
});

const trochut = localFont({
  src: "./fonts/Trochut-Regular.ttf",
  variable: "--font-trochut-regular",
  weight: "400",
});



// Rest of the code...

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} ${trochut}`}>
        {children}
      </body>
    </html>
  );
}