namespace WindowsFormsApplication2
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.userlbl = new System.Windows.Forms.Label();
            this.qualitylbl = new System.Windows.Forms.Label();
            this.animelbl = new System.Windows.Forms.Label();
            this.usernametxt = new System.Windows.Forms.TextBox();
            this.qualitytxt = new System.Windows.Forms.TextBox();
            this.animetxt = new System.Windows.Forms.TextBox();
            this.downbtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // userlbl
            // 
            this.userlbl.AutoSize = true;
            this.userlbl.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.userlbl.Location = new System.Drawing.Point(12, 9);
            this.userlbl.Name = "userlbl";
            this.userlbl.Size = new System.Drawing.Size(102, 24);
            this.userlbl.TabIndex = 0;
            this.userlbl.Text = "User name";
            this.userlbl.Click += new System.EventHandler(this.label1_Click);
            // 
            // qualitylbl
            // 
            this.qualitylbl.AutoSize = true;
            this.qualitylbl.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.qualitylbl.Location = new System.Drawing.Point(12, 53);
            this.qualitylbl.Name = "qualitylbl";
            this.qualitylbl.Size = new System.Drawing.Size(67, 24);
            this.qualitylbl.TabIndex = 0;
            this.qualitylbl.Text = "Quality";
            // 
            // animelbl
            // 
            this.animelbl.AutoSize = true;
            this.animelbl.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.animelbl.Location = new System.Drawing.Point(12, 101);
            this.animelbl.Name = "animelbl";
            this.animelbl.Size = new System.Drawing.Size(126, 24);
            this.animelbl.TabIndex = 0;
            this.animelbl.Text = "Anime Name:";
            this.animelbl.Click += new System.EventHandler(this.label1_Click);
            // 
            // usernametxt
            // 
            this.usernametxt.Location = new System.Drawing.Point(165, 13);
            this.usernametxt.Name = "usernametxt";
            this.usernametxt.Size = new System.Drawing.Size(100, 20);
            this.usernametxt.TabIndex = 1;
            // 
            // qualitytxt
            // 
            this.qualitytxt.Location = new System.Drawing.Point(165, 58);
            this.qualitytxt.Name = "qualitytxt";
            this.qualitytxt.Size = new System.Drawing.Size(49, 20);
            this.qualitytxt.TabIndex = 1;
            this.qualitytxt.Text = "720";
            this.qualitytxt.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // animetxt
            // 
            this.animetxt.Location = new System.Drawing.Point(16, 147);
            this.animetxt.Name = "animetxt";
            this.animetxt.Size = new System.Drawing.Size(249, 20);
            this.animetxt.TabIndex = 1;
            // 
            // downbtn
            // 
            this.downbtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F);
            this.downbtn.Location = new System.Drawing.Point(69, 193);
            this.downbtn.Name = "downbtn";
            this.downbtn.Size = new System.Drawing.Size(135, 56);
            this.downbtn.TabIndex = 2;
            this.downbtn.Text = "Start download";
            this.downbtn.UseVisualStyleBackColor = true;
            this.downbtn.Click += new System.EventHandler(this.downbtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.downbtn);
            this.Controls.Add(this.animetxt);
            this.Controls.Add(this.qualitytxt);
            this.Controls.Add(this.usernametxt);
            this.Controls.Add(this.qualitylbl);
            this.Controls.Add(this.animelbl);
            this.Controls.Add(this.userlbl);
            this.Name = "Form1";
            this.Text = "Nyaa batch downloader";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label userlbl;
        private System.Windows.Forms.Label qualitylbl;
        private System.Windows.Forms.Label animelbl;
        private System.Windows.Forms.TextBox usernametxt;
        private System.Windows.Forms.TextBox qualitytxt;
        private System.Windows.Forms.TextBox animetxt;
        private System.Windows.Forms.Button downbtn;
    }
}

