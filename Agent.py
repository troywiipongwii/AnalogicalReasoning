from PIL import Image, ImageChops, ImageFilter, ImageOps
import numpy as np
import random

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass
    
    def Solve(self, problem):
        
        
        if problem.problemType == '2x2':
            
            print("problem name: " + problem.name)
            prob_fig = {}
            ans_fig = {}
            prob_array = {}
            ans_array = {}
            
            
            rav_list = ['A', 'B', 'C']
            ans_list = ['1', '2', '3', '4', '5', '6']   
    
    
            for key in problem.figures:
                fig = problem.figures[key]
                image = Image.open(fig.visualFilename).convert('L')               
                arrayImage = self.centerImageArray(np.array(image))
                if key in rav_list:
                    prob_fig[key] = image
                    prob_array[key] = arrayImage
                if key in ans_list:
                    ans_fig[key] = image   
                    ans_array[key] = arrayImage          
            
            
            ATransformations = [ 
            prob_fig['A'].transpose(Image.FLIP_LEFT_RIGHT), 
            prob_fig['A'].transpose(Image.FLIP_TOP_BOTTOM), 
            prob_fig['A'].transpose(Image.ROTATE_90), 
            prob_fig['A'].transpose(Image.ROTATE_180), 
            prob_fig['A'].transpose(Image.ROTATE_270)
            ]
            
            BTransformations = [ 
            prob_fig['B'].transpose(Image.FLIP_LEFT_RIGHT), 
            prob_fig['B'].transpose(Image.FLIP_TOP_BOTTOM), 
            prob_fig['B'].transpose(Image.ROTATE_90), 
            prob_fig['B'].transpose(Image.ROTATE_180), 
            prob_fig['B'].transpose(Image.ROTATE_270)
            ]   
            
            CTransformations = [ 
            prob_fig['C'].transpose(Image.FLIP_LEFT_RIGHT), 
            prob_fig['C'].transpose(Image.FLIP_TOP_BOTTOM), 
            prob_fig['C'].transpose(Image.ROTATE_90), 
            prob_fig['C'].transpose(Image.ROTATE_180), 
            prob_fig['C'].transpose(Image.ROTATE_270)
            ]                    
        
                    
            
            if prob_fig['A'] == prob_fig['B']:
                print('A == B')
                for i in range(1,7):
                    if ans_fig[str(i)] == prob_fig['C']:
                        answer = i
                        print(answer)
                        return answer                  

                    
            elif prob_fig['A'] == prob_fig['C']:
                print('A == C')               
                for i in range(1,7):
                        if prob_fig['B'] == ans_fig[str(i)]:
                            answer = i
                            print(answer)
                            return answer
                    
                    
            elif prob_fig['A'] != prob_fig['B'] and prob_fig['A'] != prob_fig['C']:
                print('A !=C')
                
                for x in range(len(ATransformations)):
                    if prob_fig['B'] == ATransformations[x]:
                        print('B a Transformation of A')
                        trans = x
                        for i in range(1,7):
                            if ans_fig[str(i)] == CTransformations[trans]:
                                print(i)
                                return i
                            
                for x in range(len(ATransformations)):
                    if prob_fig['C'] == ATransformations[x]:
                        print('C a Transformation of A')
                        trans = x
                        for i in range(1,7):
                            if ans_fig[str(i)] == BTransformations[trans]:
                                print(i)
                                return i                
                
                               
                AtransArray = self.center_lists(ATransformations)
                BtransArray = self.center_lists(BTransformations)
                CtransArray = self.center_lists(CTransformations)
                
                compare_scoreAB = [self.compare_images(AtransArray[x], prob_array['B']) for x in range(len(AtransArray))]
                abMin = np.argmin(compare_scoreAB)
                compare_scoreCI = [self.compare_images(ans_array[x], CtransArray[abMin]) for x in ans_array]
                compare_scoreAC = [self.compare_images(AtransArray[x], prob_array['C']) for x in range(len(AtransArray))]
                acMin = np.argmin(compare_scoreAC)
                compare_scoreBI = [self.compare_images(ans_array[x], CtransArray[acMin]) for x in ans_array]                
                
                
                
                
                if len(compare_scoreAB) == compare_scoreAB.count(compare_scoreAB[0]):
                    print('All equal') 
                    print(compare_scoreAB)
                    mlist = [self.centerImageArray(np.array(ImageChops.darker(prob_fig['C'],ans_fig[x]))) for x in ans_fig]
                    mlistMin = np.argmin(mlist)
          
                    j = self.centerImageArray(np.array(ImageChops.darker(prob_fig['A'],prob_fig['B'])))
                    k = self.compare_images(j, prob_array['B'])
                    print(k)
                    
                    complist = [ self.pixels_comparison(mlist[mlistMin],ans_array[x]) for x in ans_array]    
                    mincomp = np.argmin(complist)
                    
                    if min(complist) <= k:
                        answer = mincomp + 1
                        print(answer)
                        return answer
                    else:
                        answer = mincomp + 1
                        print(answer)
                        return(answer)
    
                                    
                elif min(compare_scoreAC) < min(compare_scoreAB):
                    print('C transformation')
                    index_minCI = np.argmin(compare_scoreBI)
                    answer = index_minCI + 1
                    print(answer)
                    return answer
                elif min(compare_scoreAB) < min(compare_scoreAC):
                    print('B transformation')
                    index_minBI = np.argmin(compare_scoreCI)
                    answer = index_minBI + 1
                    print(answer)
                    return answer
                                                               
                                
        if problem.problemType == '3x3':

            print("problem name: " + problem.name)
            prob_fig = {}
            ans_fig = {}
            prob_array = {}
            ans_array = {}
        
        
            rav_list = ['A', 'B', 'C','D','E','F','G','H']
            ans_list = ['1', '2', '3', '4', '5', '6','7','8']   
        
        
            for key in problem.figures:
                fig = problem.figures[key]
                image = Image.open(fig.visualFilename).convert('L')                   
                arrayImage = self.centerImageArray(np.array(image))
                if key in rav_list:
                    prob_fig[key] = image
                    prob_array[key] = arrayImage
                if key in ans_list:
                    ans_fig[key] = image   
                    ans_array[key] = arrayImage
            
            aList = ["AB", "AC", "AD", "AE","AF",'AG','AH']
            bList = ["BC","BD","BE","BF",'BG','BH']
            cList = ["CD","CE","CF",'CG','CH']
            dList = ['DE','DF','DG','DH']
            eList = ['EF','EG','EH']
            flist = ['FG','FH']
            acompare = [ prob_array['B'],prob_array['C'],prob_array['D'],prob_array['E'],prob_array['F'],prob_array['G'],prob_array['H']]
            bcompare = [prob_array['C'],prob_array['D'],prob_array['E'],prob_array['F'],prob_array['G'],prob_array['H']]
            ccompare = [prob_array['D'],prob_array['E'],prob_array['F'],prob_array['G'],prob_array['H']]
            dcompare = [prob_array['E'],prob_array['F'],prob_array['G'],prob_array['H']]
            ecompare = [prob_array['F'],prob_array['G'],prob_array['H']]
            fcompare = [prob_array['G'],prob_array['H']]
            ghPix = self.pixels_comparison(prob_array['G'], prob_array['H'])
            ghMSE = self.compare_images(prob_array['G'], prob_array['H'])
            aDictPix = [self.pixels_comparison(prob_array['A'],x) for x in acompare]
            bDictPix = [self.pixels_comparison(prob_array['B'],x) for x in bcompare]
            cDictPix = [self.pixels_comparison(prob_array['C'],x) for x in ccompare]
            dDictPix = [self.pixels_comparison(prob_array['D'],x) for x in dcompare]
            eDictPix = [self.pixels_comparison(prob_array['E'],x) for x in ecompare]
            fDictPix = [self.pixels_comparison(prob_array['F'],x) for x in fcompare]            
            aDictMSE = [self.compare_images(prob_array['A'],x) for x in acompare]
            bDictMSE = [self.compare_images(prob_array['B'],x) for x in bcompare]
            cDictMSE = [self.compare_images(prob_array['C'],x) for x in ccompare]
            dDictMSE = [self.compare_images(prob_array['D'],x) for x in dcompare]
            eDictMSE = [self.compare_images(prob_array['E'],x) for x in ecompare]
            fDictMSE = [self.compare_images(prob_array['F'],x) for x in fcompare]
            
            ansListH = [self.pixels_comparison(prob_array['H'],ans_array[str(x)]) for x in range(1,9)]
            ansListF = [self.pixels_comparison(prob_array['F'],ans_array[str(x)]) for x in range(1,9)]
            ansListG = [self.pixels_comparison(prob_array['G'],ans_array[str(x)]) for x in range(1,9)]
            ansListE = [self.pixels_comparison(prob_array['E'],ans_array[str(x)]) for x in range(1,9)]
            
            ansMinH = np.argmin(ansListH)
            ansMinF = np.argmin(ansListF)
            ansMinG = np.argmin(ansListG)
            ansMinE = np.argmin(ansListE) 
            
            
            ''' Problem Solving for Analogical Reasoning'''
            
            '''Finding an answer with individual figure changes from frame to frame'''
            
            if aDictPix[0] == bDictPix[0]:
                answer = ansMinH + 1
                print(answer)
                return answer
            elif aDictPix[3] == 0:
                if prob_array['A'].all() == prob_array['E'].all():
                    answer = ansMinE + 1
                    print(answer)
                    return answer
                else:
                    print('circles are not squares')
                    return 2
            else:
                nextTree = 'move to sum'
                print(nextTree)
            
            
            '''Finding and answer through the aggregate change accross the entire row'''
            
            if nextTree == 'move to sum':
                sumOfRow1 = self.sum_of_row(prob_array['A'], prob_array['B'], prob_array['C'])
                sumOfRow2 = self.sum_of_row(prob_array['D'], prob_array['E'], prob_array['E'])
                sumOfPairAB = self.sum_of_pair(prob_array['A'], prob_array['B'])
                sumOfPairAC = self.sum_of_pair(prob_array['A'], prob_array['C'])
                sumOfPairBC = self.sum_of_pair(prob_array['B'], prob_array['C'])
                diffOfRow1 = self.diff_of_row(prob_array['A'], prob_array['B'], prob_array['C'])
                diffOfRow2 = self.diff_of_row(prob_array['D'], prob_array['E'], prob_array['F'])
                
                A = self.get_pixel_count(prob_array['A'])
                B = self.get_pixel_count(prob_array['B'])
                C = self.get_pixel_count(prob_array['C'])
                if sumOfRow1 == sumOfRow2:
                    print('row sums equal')
                    pass
                elif sumOfPairAB == C:
                    print('combo of AB2C')
                    pass
                elif sumOfPairAC == B:
                    print('combo of AC2B')
                    pass
                elif sumOfPairBC == A:
                    print('combo of BC2A')
                    pass
                elif diffOfRow1 == diffOfRow2:
                    print('cyclic pattern with with equal interior and changing exterior of figure')
                    answerlist = self.diff_of_ans(prob_array['G'], prob_array['H'], ans_array)
                    if min(answerlist) == diffOfRow1:
                        answer = np.argmin(answerlist) + 1
                        print(answer)
                        return(answer)
                    else:
                        answerList = [abs(diffOfRow1 - x) for x in answerlist]
                        answer = np.argmin(answerList) + 1
                        print(answer)
                        return answer
                else:
                    nextTree = 'move to differences'
                    print(nextTree)
                
                ''' finding an answer through comparing the pixel differences between pairs of frames '''
                
                answer1 = self.nearest_answerHI(eDictPix,ansListH)
                answer2 = self.nearest_answerFI(eDictPix,ansListF)
                answer3 = self.nearest_answerGI(aDictPix,ansListG)
                answer4 = self.nearest_answerEI(bDictPix,ansListE)
                
                if aDictPix[0] == dDictPix[0]:                    
                    print('AB2DE row difference equal')
                    if bDictPix[0] == eDictPix[0]:
                        print('AB2DE and BC2DE')
                        if aDictPix[2] == bDictPix[2]:
                            print('equal pair transformation across row and down column')
                            if answer1 == answer2:
                                print(' answers equal')
                                print(answer1)
                                return(answer1)
                            else:
                                print(answer1)
                                return answer1
                    else:
                        return answer1
                    
                elif aDictPix[2] == bDictPix[2]:
                    print('transformation pair equal down column')
                    print(answer2)
                    return answer2
                elif aDictPix[1] == dDictPix[1]:
                    print('transformation pair equal across row')
                    for x in prob_array:
                        if self.pixels_comparison(ans_array[str(answer3)],prob_array[x]) == 0:
                            print('answer equal to another object')
                            answerlist = [self.pixels_comparison(ans_array[str(answer3)],ans_array[str(x)]) for x in ans_array]
                            answer = self.find_second_min_list(answerlist) + 1
                            print(answer)
                            return answer
                elif (aDictPix[3] == bDictPix[1] or aDictPix[3] == bDictPix[3]) or (aDictPix[3] == cDictPix[0] or aDictPix[3] == cDictPix[2]):
                    print('Cyclic pattern where differences are equal diagonally')
                    print(answer4)
                    return answer4
                elif ( self.compare_pixels(aDictPix[3],bDictPix[1]) < .1 or self.compare_pixels(aDictPix[3],bDictPix[1]) < .1):
                    print('Cyclic pattern where differences are equal diagonally')
                    print(answer4)
                    return answer4
                else:
                    nextTree = 'move to combo'
                    print(nextTree)
                    
                '''using combinations to solve problems'''
                
                if nextTree == 'move to combo':
                    imagecombo = self.image_combo(prob_fig,prob_array)
                    imagedifference = self.change_black_to_white(prob_fig, prob_array)
                    #imagereduction = self.image_reduction(prob_fig,prob_array)
                    comboList = [imagecombo[0], imagedifference[0]]
                    #ssimList = [imagecombo[4], imagedifference[4]]
                    comboMin = np.argmin(comboList)
                    #ssimMax = np.argmax(ssimList)
                    if comboMin == 0: # and ssimMax == 0:
                        print('combo of two images')
                        answer = self.ans_combo(ans_fig, ans_array,prob_fig,prob_array,imagecombo[1])
                        print(answer)
                        return answer
                    elif comboMin == 1: # and ssimMax == 1:
                        print('difference of two images')
                        answer = self.ans_difference(ans_fig, ans_array,prob_fig,prob_array,imagedifference[1])
                        print(answer)
                        return answer
                    #elif comboMin == 2:
                        #print('reduction of two images')
                        #answer = self.ans_reduction(ans_fig, ans_array,prob_fig,prob_array,imagereduction[1])
                        #print(answer)
                        #return answer    
                else:
                    nexTree = 'move to pixel sequence'
                    print(nextTree)
                    
                
                ''' using pixel sequence to find answers'''
                
                if nextTree == 'move to pixel sequence':
                    if (self.pixels_comparison(prob_array['A'],prob_array['B']) < self.pixels_comparison(prob_array['A'],prob_array['C'])) and (self.pixels_comparison(prob_array['A'],prob_array['B']) < self.pixels_comparison(prob_array['B'],prob_array['C'])):
                        print('problem is a sequence problem')
                        for i in range(0,8):
                            if ghPix < ansListG[i]:
                                print(True)
                                answer = i + 1
                                print(answer)
                                return answer
                    else:
                        nextTree = 'last stand'
                        print(nextTree)
                    
                ''' Calculated Random Guessing '''
                
                if nextTree == 'last stand':
                    answer = random.randint(1,9)
                    print(answer)
                    return(answer)
                            
                
                
                
                
                
                    
                            
                                
                    
                    

                        
                    
                
                
            
    ''' Functions for determining transformations'''
    

    def find_nearest_list(self, list1, list2,list3,list4, four):       

        rowListAD = [abs(list1[0] - x) for x in list4]
        rowListGH = abs(list1[0] - four)
        
        
        comboListAD = [abs(list1[1] - x) for x in list4]
        

        colListAB = [abs(list1[2] - x) for x in list2]
        colListAC = [abs(list1[2] - x) for x in list3]

        diagListAB = [abs(list1[3] - x) for x in list2]
        diagListAC = [abs(list1[3] - x) for x in list3]

        rowminAD = np.argmin(rowListAD)
        colminAB = np.argmin(colListAB)
        colminAC = np.argmin(colListAC)
        diagminAB = np.argmin(diagListAB)
        diagminAC = np.argmin(diagListAC)
        combolistmin = np.argmin(comboListAD)

        if diagminAB == 1 or diagminAB == 3:
            print('Cyclic pattern')
            return 1
        elif rowListAD == 0:
            if rowListGH == 0:
                print('pattern same ab2de2gh and bc2ef2hi')
                return 2
        elif combolistmin == 1:
            print('Combo or pattern same across rows')
            return 3
        else:
            return 4

    def nearest_answerHI(self, list1,list2):
        
        ansListHI = [abs(list1[0] - x) for x in list2]
        
        minAns = np.argmin(ansListHI)
        
        answer = minAns + 1
        print(answer)
        return answer
    
    def nearest_answerGI(self, list1,list2):
        
        ansListGI = [abs(list1[1] - x) for x in list2]
        
        minAns = np.argmin(ansListGI)
        
        answer = minAns + 1
        return answer
    
    def nearest_answerEI(self, list1,list2):
        
        ansListEI = [abs(list1[3] - x) for x in list2]
        
        minAns = np.argmin(ansListEI)
        
        answer = minAns + 1
        return answer    
    
    def nearest_answerFI(self, list1,list2):
        
        ansListFI = [abs(list1[2] - x) for x in list2]
        
        minAns = np.argmin(ansListFI)
        
        answer = minAns + 1
        return answer       


    def greater_than_list(self, ans_array, prob_array):

        if self.pixels_comparison(prob_array['A'],prob_array['B']) < self.pixels_comparison(prob_array['B'],prob_array['C']):
            i = 0
            max_list = []
            while i < len(ans_array):
                m = self.pixels_comparison(prob_array['H'],ans_array[str(i)])
                if m > self.pixels_comparison(prob_array['G'],prob_array['H']):
                    max_list.append(m)
                    i +=1 
                    return m            
            
            
            
            
            
    ''' Functions for dealing with the images '''
    
    def center_lists(self, list1):
        
        listUpdate = [self.centerImageArray(np.array(list1[x])) for x in range(len(list1))]
        return listUpdate
    
    def black_white_pixel_flip(self, image):
        inverted = Image.new("1", image.size, "white")
        for x in range(0, image.size[1]):
            for y in range(0, image.size[0]):
                p1 = image.getpixel((x, y))
                if (p1 == 0):
                    inverted.putpixel((x, y), 255)
                else:
                    inverted.putpixel((x, y), 0)

        return inverted  
    
    def make_transparent(self,img):

        pixdata = img.load()

        width, height = img.size
        for y in range(height):
            for x in range(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)

    
    def pixels_comparison(self, figArray, figArray2):
        # in 'L', 255 is white
        white1 = np.count_nonzero(figArray)
        black1 = figArray.size - white1
        white2 = np.count_nonzero(figArray2)
        black2 = figArray2.size - white2
        difference = abs(black2 - black1)
        return difference
    
    def get_pixel_count(self, figArray):
        white = np.count_nonzero(figArray)
        black = figArray.size - white        
        return black    

    
    def find_nearest_neighbor(self, ans_array, array1, array2, array3):
        answer_compare = [self.pixels_comparison(x,array1) for x in ans_array]
        prob_pixels = self.pixels_comparison(array2,array3)
        nearest_list = [abs(prob_pixels - x) for x in answer_compare]
        nearestNeighbor = np.argmin(nearest_list)
        answer = nearestNeighbor + 1
        print(answer)
        return answer    
    
    def centerImageArray(self,figArray):
        figImage = Image.fromarray(figArray, "L")

        # mask
        threshold=128
        mask = figImage.point(lambda p: p < threshold and 255)

        # find edges
        edges = mask.filter(ImageFilter.FIND_EDGES)
        box = edges.getbbox()
        edges = edges.crop(box)

        # center in new image-figure
        tempImg = Image.new("L", figImage.size)

        width, height = edges.size
        fwidth, fheight = figImage.size

        tempImg.paste(edges, ((fwidth - width) // 2, (fheight - height) // 2))

        return np.array(tempImg)

    def MSE(self,arrayA, arrayB):
        return np.square(arrayA - arrayB).mean()

    def compare_images(self, arrayA, arrayB):
        # compute the mean squared error and structural similarity
        # index for the images
        m = self.MSE(arrayA, arrayB)
        
        return m
    
    def structural_similarity(self, array1, array2):
        ux = np.mean(array1)
        uy = np.mean(array2)
        uxx = ux*ux
        uyy = uy*uy
        
        xy = array1*array2
        uxy = np.mean(xy)
        
        xstd = np.std(array1)
        ystd = np.std(array2)
        xystd = np.std(xy)
        
        xv = uxx - ux * ux
        yv = uyy - uy * uy
        xyv = uxy - ux * uy
        
        C1 = (.8*255)**2
        C2 = (.9*255)**2
        
        ssim = (((2*ux*uy + C1)*(2*xyv + C2)/((uxx + uyy + C1)*(xv + yv + C2))))
        return ssim 

    
    def compare_pixels(self, list1, list2):
        
        m = (abs(list1 - list2)/list1)
        return m

    def find_min(self, ans_array, array2):
        answer_compare = [self.compare_images(ans_array[str(x)],array2) for x in range(1,9)]
        answer_compare1 = [self.pixels_comparison(ans_array[str(x)],array2) for x in range(1,9)]
        min_array = np.argmin(answer_compare)
        min_array1 = np.argmin(answer_compare1)
        
        if min_array == min_array1:
            return min_array
        else:
            return min_array1
    

    def find_second_min_array(self, ans_array, array2):
        answer_compare = [self.compare_images(ans_array[str(x+ 1)],array2) for x in range(len(ans_array))]
        answer_compare1 = answer_compare
        answer_compare1.sort()
        length = len(answer_compare)
        second_smallest = answer_compare1[length - 2]

        for i in range(length):
            if answer_compare[i] == second_smallest:
                answer = i

        answer_comparepix = [self.pixels_comparison(ans_array[str(x+ 1)],array2) for x in range(len(ans_array))]
        answer_comparepix1 = answer_comparepix
        answer_comparepix1.sort()
        length1 = len(answer_comparepix)
        second_smallestpix = answer_comparepix1[length - 2]

        for i in range(length1):
            if answer_comparepix[i] == second_smallestpix:
                answerpix = i

                resultlist = [answer,answerpix]
                return resultlist 
    
    def find_second_min_list(self, list1):
        
        list1.sort()
        length = len(list1)
        second_smallest = list1[length - 2]

        for i in range(length):
            if list1[i] == second_smallest:
                answer = i
                
                return answer
    
    
          
    def sum_of_row(self, arrayA, arrayB, arrayC):
        
        A = self.get_pixel_count(arrayA)
        B = self.get_pixel_count(arrayB)
        C = self.get_pixel_count(arrayC)
        
        sumABC = A + B + C
        
        return sumABC
    
    def sum_of_pair(self, arrayA, arrayB):
        
        A = self.get_pixel_count(arrayA)
        B = self.get_pixel_count(arrayB)
        
        sumAB = A + B
        
        return sumAB
    
    def sum_of_ans(self, arrayG, arrayH, ans_array):
        
        G = self.get_pixel_count(arrayG)
        H = self.get_pixel_count(arrayH)
        
        sumOfAns = [(G + H + self.get_pixel_count(x)) for x in ans_array]
        
        return sumOfAns
    
    def diff_of_row(self, a, b, c):
        
        ab = self.pixels_comparison( a, b)
        bc = self.pixels_comparison( b, c)
        
        difference = abs(ab - bc)
        
        return difference 
    
    def diff_of_ans(self, g, h, ans_array):
        
        gh = self.pixels_comparison( g, h)
        
        diffOfAns = [abs(gh - self.pixels_comparison(h, ans_array[x])) for x in ans_array]
        
        return diffOfAns
    
    '''Combination functions'''   
    
    def image_combo(self, prob_fig, prob_array):
        
        AB = ImageChops.darker(prob_fig['A'],prob_fig['B'])
        BC = ImageChops.darker(prob_fig['B'],prob_fig['C'])
        AC = ImageChops.darker(prob_fig['A'],prob_fig['A'])
        
        arrayAB = self.centerImageArray(np.array(ImageChops.darker(prob_fig['A'],prob_fig['B'])))
        arrayBC = self.centerImageArray(np.array(ImageChops.darker(prob_fig['B'],prob_fig['C'])))
        arrayAC = self.centerImageArray(np.array(ImageChops.darker(prob_fig['A'],prob_fig['C'])))

        ABisC = self.pixels_comparison(arrayAB, prob_array['C'])
        BCisA = self.pixels_comparison(arrayBC, prob_array['A'])
        ACisB = self.pixels_comparison(arrayAC, prob_array['B'])

        ABisC1 = self.compare_images(arrayAB, prob_array['C'])
        BCisA1 = self.compare_images(arrayBC, prob_array['A'])
        ACisB1 = self.compare_images(arrayAC, prob_array['B'])
        
        ABisC2 = self.structural_similarity(arrayAB, prob_array['C'])
        BCisA2 = self.structural_similarity(arrayBC, prob_array['A'])
        ACisB2 = self.structural_similarity(arrayAC, prob_array['B'])        
        
        

        min_list = [ABisC,BCisA,ACisB]
        min_list1 = [ABisC1,BCisA1,ACisB1]
        min_list2 = [ABisC2,BCisA2,ACisB2]
        min_value = min(min_list)
        min_index = np.argmin(min_list)
        min_value1 = min(min_list1)
        min_index1 = np.argmin(min_list1)
        min_value2 = max(min_list2)
        min_index2 = np.argmax(min_list2)
        m = [min_value,min_index,min_value1,min_index1, min_value2, min_index2]
        return m
    
    def image_reduction(self, prob_fig, prob_array):
        AB = ImageChops.lighter(prob_fig['A'],prob_fig['B'])
        BC = ImageChops.lighter(prob_fig['B'],prob_fig['C'])
        AC = ImageChops.lighter(prob_fig['A'],prob_fig['A'])
        
        arrayAB = self.centerImageArray(np.array(ImageChops.lighter(prob_fig['A'],prob_fig['B'])))
        arrayBC = self.centerImageArray(np.array(ImageChops.lighter(prob_fig['B'],prob_fig['C'])))
        arrayAC = self.centerImageArray(np.array(ImageChops.lighter(prob_fig['A'],prob_fig['C'])))

        ABisC = self.pixels_comparison(arrayAB, prob_array['C'])
        BCisA = self.pixels_comparison(arrayBC, prob_array['A'])
        ACisB = self.pixels_comparison(arrayAC, prob_array['B'])

        ABisC1 = self.compare_images(arrayAB, prob_array['C'])
        BCisA1 = self.compare_images(arrayBC, prob_array['A'])
        ACisB1 = self.compare_images(arrayAC, prob_array['B'])
        
        ABisC2 = self.structural_similarity(arrayAB, prob_array['C'])
        BCisA2 = self.structural_similarity(arrayBC, prob_array['A'])
        ACisB2 = self.structural_similarity(arrayAC, prob_array['B'])        
        
        

        min_list = [ABisC,BCisA,ACisB]
        min_list1 = [ABisC1,BCisA1,ACisB1]
        min_list2 = [ABisC2,BCisA2,ACisB2]
        min_value = min(min_list)
        min_index = np.argmin(min_list)
        min_value1 = min(min_list1)
        min_index1 = np.argmin(min_list1)
        min_value2 = max(min_list2)
        min_index2 = np.argmax(min_list2)
        m = [min_value,min_index,min_value1,min_index1, min_value2, min_index2]
        return m
    
    def change_black_to_white(self, prob_fig, prob_array):
        
        AB = self.black_white_pixel_flip(ImageChops.difference(prob_fig['A'], prob_fig['B']))
        BC = self.black_white_pixel_flip(ImageChops.difference(prob_fig['B'], prob_fig['C']))
        AC = self.black_white_pixel_flip(ImageChops.difference(prob_fig['A'], prob_fig['C']))       
        
        arrayAB = self.centerImageArray(np.array(AB))
        arrayBC = self.centerImageArray(np.array(BC))
        arrayAC = self.centerImageArray(np.array(AC))
                                      
        ABisC = self.pixels_comparison(arrayAB, prob_array['C'])
        BCisA = self.pixels_comparison(arrayBC, prob_array['A'])
        ACisB = self.pixels_comparison(arrayAC, prob_array['B'])

        ABisC1 = self.compare_images(AB, prob_array['C'])
        BCisA1 = self.compare_images(BC, prob_array['A'])
        ACisB1 = self.compare_images(AC, prob_array['B'])
        
        ABisC2 = self.structural_similarity(AB, prob_array['C'])
        BCisA2 = self.structural_similarity(BC, prob_array['A'])
        ACisB2 = self.structural_similarity(AC, prob_array['B'])        

        min_list = [ABisC,BCisA,ACisB]
        min_list1 = [ABisC1,BCisA1,ACisB1]
        min_list2 = [ABisC2,BCisA2,ACisB2]
        min_value = min(min_list)
        min_index = np.argmin(min_list)
        min_value1 = min(min_list1)
        min_index1 = np.argmin(min_list1)
        min_value2 = max(min_list2)
        min_index2 = np.argmax(min_list2)
        m = [min_value,min_index,min_value1,min_index1, min_value2, min_index2]
        return m
       
    
    ''' Answer functions for combination functions'''
    
   
    
    def ans_difference(self, ans_fig, ans_array, prob_fig,prob_array,min_index):
        
        GH = self.black_white_pixel_flip(ImageChops.difference(prob_fig['G'],prob_fig['H']))
        HI = [self.black_white_pixel_flip(ImageChops.difference(prob_fig['H'],ans_fig[str(x)])) for x in range(1,9)]
        GI = [self.black_white_pixel_flip(ImageChops.difference(prob_fig['G'],ans_fig[str(x)])) for x in range(1,9)]
        
        arrayGH = self.centerImageArray(np.array(GH))
        arrayHI = self.center_lists(HI)
        arrayGI = self.center_lists(GI)

        if min_index == 0:
            GHlist = [self.compare_images(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GH_index = np.argmin(GHlist)
            GHpixel = [self.pixels_comparison(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GHpix_index = np.argmin(GHpixel)
            GHssim = [self.structural_similarity(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GHssim_index = np.argmax(GHssim)
            if min(GHlist)== 0:
                answer1 = GH_index + 1
                print(answer1)
                return answer1
            elif min(GHpixel) == 0:
                answer2 = GHpix_index + 1
                print(answer2)
                return answer2
            elif max(GHssim) == 1:
                answer = GHssim_index + 1
                print(answer)
                return answer
            elif min(GHlist) != 0 and min(GHpixel) != 0 and max(GHssim) != 1:
                if GHssim_index == GHpix_index == GH_index:
                    answer = GH_index + 1
                    print(answer)
                    return answer
                elif GHssim_index == GHpix_index or GHssim_index == GH_index:
                    answer = GHssim_index + 1
                    print(answer)
                    return answer
                else:
                    return GHssim_index + 1


        elif min_index == 1:
            HIlist = [self.compare_images(arrayHI[x], prob_array['G']) for x in range(0,8)]
            HI_index = np.argmin(HIlist)
            HIpixel = [self.pixels_comparison(arrayHI[x], prob_array['G']) for x in range(0,8)]
            HIpix_index = np.argmin(HIpixel)
            HIssim = [self.structural_similarity(arrayHI, prob_array['G']) for x in range(0,8)]
            HIssim_index = np.argmax(HIssim)            
            if min(HIlist)== 0:
                answer1 = HI_index + 1
                print(answer1)
                return answer1
            elif min(HIpixel) == 0:
                answer2 = HIpix_index + 1
                print(answer2)
                return answer2
            elif max(HIssim) == 1:
                answer = HIssim_index + 1
                print(answer)
                return answer
            elif min(HIlist) != 0 and min(HIpixel) != 0 and max(HIssim) != 1:
                if HIssim_index == HIpix_index == HI_index:
                    answer = HI_index + 1
                    print(answer)
                    return answer
                elif HIssim_index == HIpix_index or HIssim_index == HI_index:
                    answer = HIssim_index + 1
                    print(answer)
                    return answer
                else:
                    return HIssim_index + 1

        elif min_index == 2:
            GIlist = [self.compare_images(arrayGI[x], prob_array['H']) for x in range(0,8)]
            GI_index = np.argmin(GIlist)
            GIpixel = [self.pixels_comparison(arrayGI[x], prob_array['H']) for x in range(0,8)]
            GIpix_index = np.argmin(GIpixel)
            GIssim = [self.structural_similarity(arrayGI, prob_array['H']) for x in range(0,8)]
            GIssim_index = np.argmax(GIssim)            
            if min(GIlist)== 0:
                answer1 = GI_index + 1
                print(answer1)
                return answer1
            elif min(GIpixel) == 0:
                answer2 = GIpix_index + 1
                print(answer2)
                return answer2
            elif max(GIssim) == 1:
                answer = GIssim_index + 1
                print(answer)
                return answer
            elif min(GIlist) != 0 and min(GIpixel) != 0 and max(GIssim) != 1:
                if GIssim_index == GIpix_index == GI_index:
                    answer = GH_index + 1
                    print(answer)
                    return answer
                elif GIssim_index == GIpix_index or GIssim_index == GI_index:
                    answer = GIssim_index + 1
                    print(answer)
                    return answer
                else:
                    return GIssim_index + 1  
            
    
    def ans_reduction(self, ans_fig, ans_array, prob_fig,prob_array,min_index):

        GH = ImageChops.lighter(prob_fig['G'],prob_fig['H'])

        HI = [ImageChops.lighter(prob_fig['H'],ans_fig[str(x)]) for x in range(1,9)]
        GI = [ImageChops.lighter(prob_fig['G'],ans_fig[str(x)]) for x in range(1,9)]
        
        arrayGH = self.centerImageArray(np.array(GH))
        arrayHI = self.center_lists(HI)
        arrayGI = self.center_lists(GI)        


        if min_index == 0:
            GHlist = [self.compare_images(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GH_index = np.argmin(GHlist)
            GHpixel = [self.pixels_comparison(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GHpix_index = np.argmin(GHpixel)
            GHssim = [self.structural_similarity(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GHssim_index = np.argmax(GHssim)
            if min(GHlist)== 0:
                answer1 = GH_index + 1
                print(answer1)
                return answer1
            elif min(GHpixel) == 0:
                answer2 = GHpix_index + 1
                print(answer2)
                return answer2
            elif max(GHssim) == 1:
                answer = GHssim_index + 1
                print(answer)
                return answer
            elif min(GHlist) != 0 and min(GHpixel) != 0 and max(GHssim) != 1:
                if GHssim_index == GHpix_index == GH_index:
                    answer = GH_index + 1
                    print(answer)
                    return answer
                elif GHssim_index == GHpix_index or GHssim_index == GH_index:
                    answer = GHssim_index + 1
                    print(answer)
                    return answer
                else:
                    return GHssim_index + 1
    
    
        elif min_index == 1:
            HIlist = [self.compare_images(arrayHI[x], prob_array['G']) for x in range(0,8)]
            HI_index = np.argmin(HIlist)
            HIpixel = [self.pixels_comparison(arrayHI[x], prob_array['G']) for x in range(0,8)]
            HIpix_index = np.argmin(HIpixel)
            HIssim = [self.structural_similarity(arrayHI, prob_array['G']) for x in range(0,8)]
            HIssim_index = np.argmax(HIssim)            
            if min(HIlist)== 0:
                answer1 = HI_index + 1
                print(answer1)
                return answer1
            elif min(HIpixel) == 0:
                answer2 = HIpix_index + 1
                print(answer2)
                return answer2
            elif max(HIssim) == 1:
                answer = HIssim_index + 1
                print(answer)
                return answer
            elif min(HIlist) != 0 and min(HIpixel) != 0 and max(HIssim) != 1:
                if HIssim_index == HIpix_index == HI_index:
                    answer = HI_index + 1
                    print(answer)
                    return answer
                elif HIssim_index == HIpix_index or HIssim_index == HI_index:
                    answer = HIssim_index + 1
                    print(answer)
                    return answer
                else:
                    return HIssim_index + 1
    
        elif min_index == 2:
            GIlist = [self.compare_images(arrayGI[x], prob_array['H']) for x in range(0,8)]
            GI_index = np.argmin(GIlist)
            GIpixel = [self.pixels_comparison(arrayGI[x], prob_array['H']) for x in range(0,8)]
            GIpix_index = np.argmin(GIpixel)
            GIssim = [self.structural_similarity(arrayGI, prob_array['H']) for x in range(0,8)]
            GIssim_index = np.argmax(GIssim)            
            if min(GIlist)== 0:
                answer1 = GI_index + 1
                print(answer1)
                return answer1
            elif min(GIpixel) == 0:
                answer2 = GIpix_index + 1
                print(answer2)
                return answer2
            elif max(GIssim) == 1:
                answer = GIssim_index + 1
                print(answer)
                return answer
            elif min(GIlist) != 0 and min(GIpixel) != 0 and max(GIssim) != 1:
                if GIssim_index == GIpix_index == GI_index:
                    answer = GH_index + 1
                    print(answer)
                    return answer
                elif GIssim_index == GIpix_index or GIssim_index == GI_index:
                    answer = GIssim_index + 1
                    print(answer)
                    return answer
                else:
                    return GIssim_index + 1
                
    def ans_combo(self, ans_fig, ans_array, prob_fig,prob_array,min_index):

        GH = ImageChops.darker(prob_fig['G'],prob_fig['H'])

        HI = [ImageChops.darker(prob_fig['H'],ans_fig[str(x)]) for x in range(1,9)]
        GI = [ImageChops.darker(prob_fig['G'],ans_fig[str(x)]) for x in range(1,9)]
        
        arrayGH = self.centerImageArray(np.array(GH))
        arrayHI = self.center_lists(HI)
        arrayGI = self.center_lists(GI)        

        if min_index == 0:
            GHlist = [self.compare_images(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GH_index = np.argmin(GHlist)
            GHpixel = [self.pixels_comparison(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GHpix_index = np.argmin(GHpixel)
            GHssim = [self.structural_similarity(arrayGH, ans_array[str(x)]) for x in range(1,9)]
            GHssim_index = np.argmax(GHssim)
            if min(GHlist)== 0:
                answer1 = GH_index + 1
                print(answer1)
                return answer1
            elif min(GHpixel) == 0:
                answer2 = GHpix_index + 1
                print(answer2)
                return answer2
            elif max(GHssim) == 1:
                answer = GHssim_index + 1
                print(answer)
                return answer
            elif min(GHlist) != 0 and min(GHpixel) != 0 and max(GHssim) != 1:
                if GHssim_index == GHpix_index == GH_index:
                    answer = GH_index + 1
                    print(answer)
                    return answer
                elif GHssim_index == GHpix_index or GHssim_index == GH_index:
                    answer = GHssim_index + 1
                    print(answer)
                    return answer
                else:
                    return GHssim_index + 1
    
    
        elif min_index == 1:
            HIlist = [self.compare_images(arrayHI[x], prob_array['G']) for x in range(0,8)]
            HI_index = np.argmin(HIlist)
            HIpixel = [self.pixels_comparison(arrayHI[x], prob_array['G']) for x in range(0,8)]
            HIpix_index = np.argmin(HIpixel)
            HIssim = [self.structural_similarity(arrayHI, prob_array['G']) for x in range(0,8)]
            HIssim_index = np.argmax(HIssim)            
            if min(HIlist)== 0:
                answer1 = HI_index + 1
                print(answer1)
                return answer1
            elif min(HIpixel) == 0:
                answer2 = HIpix_index + 1
                print(answer2)
                return answer2
            elif max(HIssim) == 1:
                answer = HIssim_index + 1
                print(answer)
                return answer
            elif min(HIlist) != 0 and min(HIpixel) != 0 and max(HIssim) != 1:
                if HIssim_index == HIpix_index == HI_index:
                    answer = HI_index + 1
                    print(answer)
                    return answer
                elif HIssim_index == HIpix_index or HIssim_index == HI_index:
                    answer = HIssim_index + 1
                    print(answer)
                    return answer
                else:
                    return HIssim_index + 1
    
        elif min_index == 2:
            GIlist = [self.compare_images(arrayGI[x], prob_array['H']) for x in range(0,8)]
            GI_index = np.argmin(GIlist)
            GIpixel = [self.pixels_comparison(arrayGI[x], prob_array['H']) for x in range(0,8)]
            GIpix_index = np.argmin(GIpixel)
            GIssim = [self.structural_similarity(arrayGI, prob_array['H']) for x in range(0,8)]
            GIssim_index = np.argmax(GIssim)            
            if min(GIlist)== 0:
                answer1 = GI_index + 1
                print(answer1)
                return answer1
            elif min(GIpixel) == 0:
                answer2 = GIpix_index + 1
                print(answer2)
                return answer2
            elif max(GIssim) == 1:
                answer = GIssim_index + 1
                print(answer)
                return answer
            elif min(GIlist) != 0 and min(GIpixel) != 0 and max(GIssim) != 1:
                if GIssim_index == GIpix_index == GI_index:
                    answer = GH_index + 1
                    print(answer)
                    return answer
                elif GIssim_index == GIpix_index or GIssim_index == GI_index:
                    answer = GIssim_index + 1
                    print(answer)
                    return answer
                else:
                    return GIssim_index + 1     
        
        