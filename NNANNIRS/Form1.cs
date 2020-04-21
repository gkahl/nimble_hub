using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;

namespace NNANNIRS
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
            textBox1.Text = trackBar1.Value.ToString();
            textBox2.Text = trackBar2.Value.ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (pictureBox3.Visible == false)
            {
                pictureBox3.Visible = true;
            }
            else
            {
                pictureBox3.Visible = false;
            }
           
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = pictureBox2.InitialImage;
            pictureBox3.Image = pictureBox3.InitialImage;
            richTextBox1.Text = "";
            richTextBox2.Text = "";
            richTextBox3.Text = "";
            richTextBox4.Text = "";
            richTextBox5.Text = "";
            richTextBox6.Text = "";
            richTextBox7.Text = "";
            richTextBox8.Text = "";
            richTextBox9.Text = "";
            richTextBox10.Text = "";
            richTextBox11.Text = "";
            richTextBox12.Text = "";
            richTextBox13.Text = "";
            richTextBox14.Text = "";
            richTextBox15.Text = "";
            richTextBox16.Text = "";
            richTextBox17.Text = "";
            richTextBox18.Text = "";
            richTextBox19.Text = "";
            richTextBox20.Text = "";
            richTextBox21.Text = "";
            richTextBox22.Text = "";
            richTextBox23.Text = "";
            richTextBox24.Text = "";


        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox6.Text = "0";
            if (File.Exists("/home/pi/nimble_hub/zero.sh"))
            {
                var zimble = Process.Start("/home/pi/nimble_hub/zero.sh" + " " + richTextBox1.Text);
                zimble.WaitForExit();
            }
            string path = "/home/pi/nimble_hub/outputs/log.txt";
            if (File.Exists(path))
            {

                string logText = System.IO.File.ReadAllText(path);
                string[] splitLines = logText.Split('\n');
                for (int i = 0; i < splitLines.Length; i++)
                {
                    string[] splitText = splitLines[i].Split('|');
                    richTextBox1.Text = splitText[0];//name
                    //richTextBox7.Text = splitText[1];//height
                    richTextBox7.Text = Math.Round(Double.Parse(splitText[1]), 4).ToString();
                    //richTextBox3.Text = splitText[2];//vol
                    richTextBox3.Text = Math.Round(Double.Parse(splitText[2]), 4).ToString();
                    //richTextBox8.Text = splitText[3];//area
                    richTextBox8.Text = Math.Round(Double.Parse(splitText[3]), 4).ToString();
                    // richTextBox4.Text = splitText[4];//color
                    richTextBox4.Text = Math.Round(Double.Parse(splitText[4]), 4).ToString();
                    String[] shapeNames = { "Triangle", "Rectangle", "Pentagon", "Hexagon", "Circle" };
                    richTextBox5.Text = shapeNames[Int32.Parse(splitText[5])];//shape
                    richTextBox2.Text = splitText[6];//desc
                    richTextBox6.Text = splitText[7];//count
                }
                pictureBox2.ImageLocation = "/home/pi/nimble_hub/outputs/color_image.jpg";
                pictureBox3.ImageLocation = "/home/pi/nimble_hub/outputs/bw.jpg";
            }
            else
            {
                richTextBox1.Text = "didnt read";//name
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox11.Text = "0";
            var zimble2 = Process.Start("/home/pi/nimble_hub/zero.sh" +" "+ richTextBox16.Text);
            zimble2.WaitForExit();
            string path = "/home/pi/nimble_hub/outputs/log.txt";
            if (File.Exists(path))
            {

                string logText = System.IO.File.ReadAllText(path);
                string[] splitLines = logText.Split('\n');
                for (int i = 0; i < splitLines.Length; i++)
                {
                    string[] splitText = splitLines[i].Split('|');
                    richTextBox1.Text = splitText[0];//name
                    //richTextBox7.Text = splitText[1];//height
                    richTextBox7.Text = Math.Round(Double.Parse(splitText[1]), 4).ToString();
                    //richTextBox3.Text = splitText[2];//vol
                    richTextBox3.Text = Math.Round(Double.Parse(splitText[2]), 4).ToString();
                    //richTextBox8.Text = splitText[3];//area
                    richTextBox8.Text = Math.Round(Double.Parse(splitText[3]), 4).ToString();
                    // richTextBox4.Text = splitText[4];//color
                    richTextBox4.Text = Math.Round(Double.Parse(splitText[4]), 4).ToString();
                    String[] shapeNames = { "Triangle", "Rectangle", "Pentagon", "Hexagon", "Circle" };
                    richTextBox5.Text = shapeNames[Int32.Parse(splitText[5])];//shape
                    richTextBox2.Text = splitText[6];//desc
                    richTextBox6.Text = splitText[7];//count
                }
                pictureBox2.ImageLocation = "/home/pi/nimble_hub/outputs/color_image.jpg";
                pictureBox3.ImageLocation = "/home/pi/nimble_hub/outputs/bw.jpg";
            }
            else
            {
                richTextBox1.Text = "didnt read";//name
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox19.Text = "0";
            var zimble3 = Process.Start("/home/pi/nimble_hub/zero.sh" + " " + richTextBox24.Text);
            zimble3.WaitForExit();
            string path = "/home/pi/nimble_hub/outputs/log.txt";
            if (File.Exists(path))
            {

                string logText = System.IO.File.ReadAllText(path);
                string[] splitLines = logText.Split('\n');
                for (int i = 0; i < splitLines.Length; i++)
                {
                    string[] splitText = splitLines[i].Split('|');
                    richTextBox1.Text = splitText[0];//name
                    //richTextBox7.Text = splitText[1];//height
                    richTextBox7.Text = Math.Round(Double.Parse(splitText[1]), 4).ToString();
                    //richTextBox3.Text = splitText[2];//vol
                    richTextBox3.Text = Math.Round(Double.Parse(splitText[2]), 4).ToString();
                    //richTextBox8.Text = splitText[3];//area
                    richTextBox8.Text = Math.Round(Double.Parse(splitText[3]), 4).ToString();
                    // richTextBox4.Text = splitText[4];//color
                    richTextBox4.Text = Math.Round(Double.Parse(splitText[4]), 4).ToString();
                    String[] shapeNames = { "Triangle", "Rectangle", "Pentagon", "Hexagon", "Circle" };
                    richTextBox5.Text = shapeNames[Int32.Parse(splitText[5])];//shape
                    richTextBox2.Text = splitText[6];//desc
                    richTextBox6.Text = splitText[7];//count
                }
                pictureBox2.ImageLocation = "/home/pi/nimble_hub/outputs/color_image.jpg";
                pictureBox3.ImageLocation = "/home/pi/nimble_hub/outputs/bw.jpg";
            }
            else
            {
                richTextBox1.Text = "didnt read";//name
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (File.Exists("/home/pi/nimble_hub/run.sh"))
            {
                var nimble = Process.Start("/home/pi/nimble_hub/run.sh" +" "+ trackBar1.Value.ToString() + " " + trackBar2.Value.ToString());
                nimble.WaitForExit();
            }
            string path = "/home/pi/nimble_hub/outputs/log.txt";
            if (File.Exists(path))
            {
                
                string logText = System.IO.File.ReadAllText(path);
                string[] splitLines = logText.Split('\n');
                for(int i = 0; i < splitLines.Length; i++)
                {
                    string[] splitText = splitLines[i].Split('|');
                    richTextBox1.Text = splitText[0];//name
                    //richTextBox7.Text = splitText[1];//height
                    richTextBox7.Text = Math.Round(Double.Parse(splitText[1]),4).ToString();
                    //richTextBox3.Text = splitText[2];//vol
                    richTextBox3.Text = Math.Round(Double.Parse(splitText[2]), 4).ToString();
                    //richTextBox8.Text = splitText[3];//area
                    richTextBox8.Text = Math.Round(Double.Parse(splitText[3]), 4).ToString();
                    // richTextBox4.Text = splitText[4];//color
                    richTextBox4.Text = Math.Round(Double.Parse(splitText[4]), 4).ToString();
                    String[] shapeNames = { "Triangle", "Rectangle", "Pentagon", "Hexagon", "Circle" };
                    richTextBox5.Text = shapeNames[Int32.Parse(splitText[5])];//shape
                    richTextBox2.Text = splitText[6];//desc
                    richTextBox6.Text = splitText[7];//count
                }
                pictureBox2.ImageLocation = "/home/pi/nimble_hub/outputs/color_image.jpg";
                pictureBox3.ImageLocation = "/home/pi/nimble_hub/outputs/bw.jpg";
            }
            else
            {
                richTextBox1.Text = "didnt read";//name
            }
           
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            textBox1.Text = trackBar1.Value.ToString();
            
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            textBox2.Text = trackBar2.Value.ToString();
        }
        int clickTimes = 0;
        private void button7_Click(object sender, EventArgs e)
        {
            
            if (clickTimes == 0)
            {
                button7.Text = "Are you sure!?";
                clickTimes++;
            }
            else if(clickTimes == 1)
            {
                if (File.Exists("/home/pi/nimble_hub/clear.sh"))
                {
                    var climble = Process.Start("/home/pi/nimble_hub/clear.sh");
                    climble.WaitForExit();
                }
                button7.Text = "Clear Logs";
                clickTimes = 0;
            }
        }

        
        int oysterEgg = 0;
        private void label1_Click(object sender, EventArgs e)
        {
            oysterEgg++;
            if(oysterEgg > 10)
            {
                label1.Text = "Programming by:";
                richTextBox1.Text = "Holden Dandurand";
                richTextBox2.Text = "Robb Crochiere";
                richTextBox16.Text = "Greg Franklin Kahl";
                //pictureBox2.ImageLocation = "C:/Users/Holden/Desktop/dnd/party.jpg";
            }
        }
    }
}
