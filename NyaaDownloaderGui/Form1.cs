using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void downbtn_Click(object sender, EventArgs e)
        {
            string quality;
            string animename;
            string username;

            if(usernametxt.Text.Length < 1 || animetxt.Text.Length < 1)
            {
                MessageBox.Show("At least one of the fields is empty, please enter the required information");
                return;
            }
            quality = qualitytxt.Text;
            animename = animetxt.Text;
            username = usernametxt.Text;

            string command = username + " " + quality + " " + animename;
            MessageBox.Show("Starting download");
            ProcessStartInfo info = new ProcessStartInfo(@"nyaa.exe", @command);
            Process process = new Process();
            process.StartInfo = info;
            process.Start();

        }
    }
}
