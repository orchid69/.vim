Vim�UnDo� s@�I,	F�һ��7H�L���2ɑ�u�                    H       H   H   H    X��    _�                            ����                                                                                                                                                                                                                                                                                                                                                             X�q�     �         "      SERVER=192.168.11.45�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�r     �         #       �         "    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�r     �         #    �         #    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             X�r     �                HOME5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�r     �         #      DIR=/home/satoshi5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�rN     �                4rsync -rauvz satoshi@$SERVER:/home/satoshi/.i3 $DIR/5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             X�rO     �                5rsync -rauvz satoshi@$SERVER:/home/satoshi/.vim $DIR/5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             X�rP     �                6rsync -auvz satoshi@$SERVER:/home/satoshi/.vimrc $DIR/5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             X�rQ     �                <rsync -rauvz satoshi@$SERVER:/home/satoshi/.vimperator $DIR/5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             X�rQ     �                =rsync -auvz satoshi@$SERVER:/home/satoshi/.vimperatorrc $DIR/5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             X�rR     �                Drsync -rauvz satoshi@$SERVER:/home/satoshi/dircolors-solarized $DIR/5�_�                    !        ����                                                                                                                                                                                                                                                                                                                                                             X�rT     �       "          6rsync -auvz satoshi@$SERVER:/home/satoshi/.zshrc $DIR/5�_�                    "        ����                                                                                                                                                                                                                                                                                                                                                             X�rU     �   !   #          9rsync -auvz satoshi@$SERVER:/home/satoshi/.zaliases $DIR/5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X�rc     �         #      <rsync -rauvz satoshi@$SERVER:$HOME/dircolors-solarized $DIR/5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V        X�r�     �                echo "install sshfs"   sudo apt-get install sshfs    5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                 V        X�r�     �   
           �   
           5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V        X�r�     �         #    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                   V        X�r�     �                echo "install zsh"   sudo apt-get install zsh    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        X�r�     �         !    �         !    5�_�                            ����                                                                                                                                                                                                                                                                                                                            !           !           V        X�r�     �         %       �         $    5�_�                           ����                                                                                                                                                                                                                                                                                                                            "           "           V        X�r�     �         %      echo ""5�_�                           ����                                                                                                                                                                                                                                                                                                                            "           "           V        X�r�     �         &       �         %    5�_�                           ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�s     �         &      ln -s $HOME/5�_�                          ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�sL     �         &      ln -s $HOME/dotfiles/.i3 .....5�_�                           ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�sP     �         '       �         &    5�_�                            ����                                                                                                                                                                                                                                                                                                                            $           $           V        X�s]     �                echo "setup i3"5�_�                             ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�s^     �                ,rsync -rauvz satoshi@$SERVER:$HOME/.i3 $DIR/5�_�      !                      ����                                                                                                                                                                                                                                                                                                                            "           "           V        X�sc     �         %      ln -s $HOME/dotfiles/.5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                            "           "           V        X�se     �         &       �         %    5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�sj     �         &    �         &    5�_�   "   $           #           ����                                                                                                                                                                                                                                                                                                                            $           $           V        X�sk     �                ln -s 5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�so     �         &      ln -s $HOME/dotfiles/.vim .5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�sr     �         &    5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                            $           $           V        X�st     �         (       �         '    5�_�   &   )           '           ����                                                                                                                                                                                                                                                                                                                            %           %           V        X�sv     �                ln5�_�   '   *   (       )           ����                                                                                                                                                                                                                                                                                                                            $           $           V        X�sx     �         '    �         '    5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                            %           %           V        X�s}     �         (      ln -s $HOME/dotfiles/.vim .5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                            %           %           V        X�s�     �         (    �         (    5�_�   +   -           ,           ����                                                                                                                                                                                                                                                                                                                            &           &           V        X�s�     �         )      "ln -s $HOME/dotfiles/.vimperator .5�_�   ,   .           -      !    ����                                                                                                                                                                                                                                                                                                                            &           &           V        X�s�     �         *       �         )    5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                            (           (           V        X�s�     �                ln5�_�   .   0           /           ����                                                                                                                                                                                                                                                                                                                            '           '           V        X�s�     �         *    �         *    5�_�   /   1           0      "    ����                                                                                                                                                                                                                                                                                                                            (           (           V        X�s�     �         +      "ln -s $HOME/dotfiles/.vimperator .5�_�   0   2           1           ����                                                                                                                                                                                                                                                                                                                            (           (           V        X�s�     �                echo "start vim setup"5�_�   1   3           2           ����                                                                                                                                                                                                                                                                                                                            '           '           V        X�s�     �                -rsync -rauvz satoshi@$SERVER:$HOME/.vim $DIR/5�_�   2   4           3           ����                                                                                                                                                                                                                                                                                                                            &           &           V        X�s�     �                .rsync -auvz satoshi@$SERVER:$HOME/.vimrc $DIR/5�_�   3   5           4           ����                                                                                                                                                                                                                                                                                                                            %           %           V        X�s�     �                 5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                            $           $           V        X�s�     �                echo "start vimperator setup"5�_�   5   7           6           ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�s�     �                4rsync -rauvz satoshi@$SERVER:$HOME/.vimperator $DIR/5�_�   6   8           7           ����                                                                                                                                                                                                                                                                                                                            "           "           V        X�s�     �                5rsync -auvz satoshi@$SERVER:$HOME/.vimperatorrc $DIR/5�_�   7   9           8           ����                                                                                                                                                                                                                                                                                                                            !           !           V        X�s�     �                 5�_�   8   :           9           ����                                                                                                                                                                                                                                                                                                                                                    V        X�s�     �                echo "set dircolors"5�_�   9   ;           :           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �                ;rsync -auvz satoshi@$SERVER:$HOME/dircolors-solarized $DIR/5�_�   :   <           ;           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �                Aln -sf $DIR/dircolors-solarized/dircolors.256dark $DIR/.dircolors5�_�   ;   =           <           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �                 5�_�   <   >           =           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �                 �             5�_�   =   ?           >           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �                ln 5�_�   >   @           ?           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �              �              5�_�   ?   A           @      "    ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �         !      "ln -s $HOME/dotfiles/.vimperator .5�_�   @   B           A          ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �         !    �         !    5�_�   A   C           B          ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �         "      ln -s $HOME/dotfiles/.zshrc .5�_�   B   D           C           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �                echo "setup zsh"5�_�   C   E           D           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�     �                .rsync -auvz satoshi@$SERVER:$HOME/.zshrc $DIR/5�_�   D   F           E           ����                                                                                                                                                                                                                                                                                                                                                  V        X�s�    �                1rsync -auvz satoshi@$SERVER:$HOME/.zaliases $DIR/5�_�   E   G           F          ����                                                                                                                                                                                                                                                                                                                                                             X�t7    �                 chsh -s /usr/bin/zsh5�_�   F   H           G           ����                                                                                                                                                                                                                                                                                                                                                 v       X��     �      	      	   echo "install i3"   sudo apt-get install i3       echo "install sshfs"   sudo apt-get install sshfs       echo "install zsh"   sudo apt-get install zsh    5�_�   G               H           ����                                                                                                                                                                                                                                                                                                                                                 v       X��    �                 5�_�   '           )   (           ����                                                                                                                                                                                                                                                                                                                            %           %           V        X�sw     �         '    �         '      ln -s $HOME/dotfiles/.vim .5�_�                            ����                                                                                                                                                                                                                                                                                                                            #           #           V        X�sB     �         &      dotfiles/.i3 .....5�_�                   	       ����                                                                                                                                                                                                                                                                                                                                                             X�r�     �   	   
   #    �   	   
   #      ,rsync -rauvz satoshi@$SERVER:$HOME/.i3 $DIR/       echo "install sshfs"5�_�                       5    ����                                                                                                                                                                                                                                                                                                                                                             X�rm     �         #      ,rsync -auvz satoshi@$SERVER:$HOME/.dir $DIR/5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             X�r5     �                ,rsync -rauvz satoshi@$SERVER:/HOME/.i3 $DIR/5��