Vim�UnDo� ��7��'���Z�[����
'�J�1nNS�8�   �   `ax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5, label="BNN")   }         .       .   .   .    X��    _�                     {        ����                                                                                                                                                                                                                                                                                                                            {           {           V        X��     �   z   |          n1,n2,n3,n4 = fmap1.data.shape5�_�                    {        ����                                                                                                                                                                                                                                                                                                                            {           {           V        X��     �   {   }   ~    �   {   |   ~    5�_�                    |        ����                                                                                                                                                                                                                                                                                                                            |           |           V        X��     �   {   }           # n1,n2,n3,n4 = fmap1.data.shape5�_�                    |       ����                                                                                                                                                                                                                                                                                                                            |           |           V        X��     �   {   }         n1,n2,n3,n4 = fmap1.data.shape5�_�                    l       ����                                                                                                                                                                                                                                                                                                                            |           |           V        X��     �   l   n       �   l   m       5�_�                    l        ����                                                                                                                                                                                                                                                                                                                            l           l           V        X��     �   k   m          n1,n2,n3,n4 = fmap1.data.shape5�_�                    m       ����                                                                                                                                                                                                                                                                                                                            l           l           V        X��    �   l   n   �      n1,n2,n3,n4 = fmap1.data.shape5�_�      	              ~   9    ����                                                                                                                                                                                                                                                                                                                                                             X��    �   }      �      Sax.hist(fmap2.data.reshape(n1*n2*n3*n4),normed=True,bins=10,color='blue',alpha=0.5)5�_�                 	   �       ����                                                                                                                                                                                                                                                                                                                                                             X��     �                 fig.savefig('hist_fmap2.pdf')5�_�   	      
          ~       ����                                                                                                                                                                                                                                                                                                                            ~           ~           V        X��     �   }      �      Sax.hist(fmap2.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5)5�_�                    }        ����                                                                                                                                                                                                                                                                                                                            }           }           V        X��     �   |   ~          n1,n2,n3,n4 = fmap2.data.shape5�_�                    |        ����                                                                                                                                                                                                                                                                                                                            |           |           V        X��     �   {   }           # n1,n2,n3,n4 = fmap1.data.shape5�_�                    x        ����                                                                                                                                                                                                                                                                                                                            |           |           V        X��     �   w   x           fmap11 = bn1(conv1(x),test=True)5�_�                    ~        ����                                                                                                                                                                                                                                                                                                                            {           {           V        X��     �   }   ~          M# ax.hist(fmap11.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='green')5�_�                    l        ����                                                                                                                                                                                                                                                                                                                            l           l           V        X���     �   k   m           # n1,n2,n3,n4 = fmap1.data.shape5�_�                    m        ����                                                                                                                                                                                                                                                                                                                            m           m           V        X���     �   l   n          n1,n2,n3,n4 = fmap2.data.shape5�_�                    n       ����                                                                                                                                                                                                                                                                                                                            m           m           V        X���    �   m   o   ~      Rax.hist(fmap2.data.reshape(n1*n2*n3*n4),normed=True,bins=10,color='red',alpha=0.5)5�_�                    }        ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }      ~    �   }   ~   ~    5�_�                    ~        ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }   ~          Sax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5)5�_�                    }        ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }      ~    5�_�                    ~        ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }             5�_�                    ~       ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }            ax.set_xlabel()5�_�                    ~       ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }            ax.set_xlabel('')5�_�                    ~       ����                                                                                                                                                                                                                                                                                                                                                             X���     �   ~   �       �   ~          5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���     �   ~   �   �      ax.set_xlabel('x')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���     �   ~   �   �      ax.set_ylabel('x')5�_�                    }   R    ����                                                                                                                                                                                                                                                                                                                                                             X��     �   |   ~   �      Sax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5)5�_�                    }   \    ����                                                                                                                                                                                                                                                                                                                                                             X��!     �   |   ~   �      ]ax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5, label='')5�_�                     }   [    ����                                                                                                                                                                                                                                                                                                                                                             X��9     �   |   ~   �      ]ax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5, label="")5�_�      !               n   Q    ����                                                                                                                                                                                                                                                                                                                                                             X��D     �   m   o   �      Rax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=10,color='red',alpha=0.5)5�_�       "           !   n   Z    ����                                                                                                                                                                                                                                                                                                                                                             X��M    �   m   o   �      \ax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=10,color='red',alpha=0.5, label="")5�_�   !   #           "   }        ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }      �       �   }      �    5�_�   "   $           #   ~   
    ����                                                                                                                                                                                                                                                                                                                                                             X���     �   }      �      ax.legend()5�_�   #   %           $   ~       ����                                                                                                                                                                                                                                                                                                                                                             X���    �   }      �      ax.legend("")5�_�   $   &           %   ~   
    ����                                                                                                                                                                                                                                                                                                                                                             X��     �   }      �      ax.legend("best")5�_�   %   '           &   ~       ����                                                                                                                                                                                                                                                                                                                                                             X��     �   }      �      ax.legend(loc="best")5�_�   &   (           '   ~       ����                                                                                                                                                                                                                                                                                                                                                             X��    �   }      �      ax.legend(loc="")5�_�   '   )           (   �       ����                                                                                                                                                                                                                                                                                                                            `           o          v       X���     �   �              fig.savefig('hist_fmap1.pdf')5�_�   (   *           )   {        ����                                                                                                                                                                                                                                                                                                                            {           {           V        X���     �   z   |          n1,n2,n3,n4 = fmap1.data.shape5�_�   )   +           *   |        ����                                                                                                                                                                                                                                                                                                                            |           |           V        X���     �   {   }           # n1,n2,n3,n4 = fmap2.data.shape5�_�   *   ,           +   l        ����                                                                                                                                                                                                                                                                                                                            l           l           V        X���     �   k   m          n1,n2,n3,n4 = fmap1.data.shape5�_�   +   -           ,   m        ����                                                                                                                                                                                                                                                                                                                            m           m           V        X���     �   l   n           # n1,n2,n3,n4 = fmap2.data.shape5�_�   ,   .           -   n       ����                                                                                                                                                                                                                                                                                                                            m           m           V        X��     �   m   o   �      gax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=10,color='red',alpha=0.5, label="BinaryFDCNN")5�_�   -               .   }       ����                                                                                                                                                                                                                                                                                                                            m           m           V        X��    �   |   ~   �      `ax.hist(fmap1.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5, label="BNN")5�_�   	             
   ~        ����                                                                                                                                                                                                                                                                                                                                                  V        X��     �   }             U# ax.hist(fmap2.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='blue',alpha=0.5)5�_�   
                          ����                                                                                                                                                                                                                                                                                                                                                  V        X��     �   ~   �          Kax.hist(fmap11.data.reshape(n1*n2*n3*n4),normed=True,bins=50,color='green')5��